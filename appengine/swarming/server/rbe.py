# Copyright 2022 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.
"""Functionality related to RBE Scheduler."""

import collections
import hashlib
import logging
import random

from google.appengine.api import app_identity
from google.appengine.ext import ndb
from google.protobuf import duration_pb2
from google.protobuf import json_format
from google.protobuf import timestamp_pb2

from components import datastore_utils
from components import utils

from proto.config import pools_pb2
from proto.internals import rbe_pb2
from server import pools_config
from server import task_pack
from server.constants import OR_DIM_SEP


# RBE related settings of some concrete bot.
RBEBotConfig = collections.namedtuple(
    'RBEBotConfig',
    [
        # Full RBE instance name to poll tasks from.
        'instance',
        # If True, check the Swarming scheduler queue before switching to RBE.
        'hybrid_mode',
    ])


def get_rbe_config_for_bot(bot_id, pools):
  """Returns an RBE instance (and related parameters) to use for the given bot.

  If the bot should not be using RBE, returns None.

  Args:
    bot_id: ID of the bot as a string.
    pools: pool IDs the bot belongs to.

  Returns:
    An RBEBotConfig tuple or None if the bot should not be using RBE.
  """
  BotMode = pools_pb2.Pool.RBEMigration.BotModeAllocation.BotMode

  # This can happen during a handshake with a broken/misconfigured bot.
  if not pools:
    return None

  # This an int in range [0, 100).
  bot_rand = _quasi_random_100(bot_id)

  def derive_mode(allocs):
    if not allocs:
      return BotMode.SWARMING

    # This config should be validated already and all percents should sum up
    # to 100. See pools_config.py.
    per_mode = {}
    for alloc in allocs:
      assert alloc.mode not in per_mode, alloc
      assert 0 <= alloc.percent <= 100, alloc
      per_mode[alloc.mode] = alloc.percent
    percent_swarming = per_mode.get(BotMode.SWARMING, 0)
    percent_hybrid = per_mode.get(BotMode.HYBRID, 0)
    percent_rbe = per_mode.get(BotMode.RBE, 0)
    assert percent_swarming + percent_hybrid + percent_rbe == 100, allocs

    # Pick the mode depending on what subrange the bot falls into in
    # [---SWARMING---|---HYBRID---|---RBE---].
    if bot_rand < percent_swarming:
      return BotMode.SWARMING
    if bot_rand < percent_swarming + percent_hybrid:
      return BotMode.HYBRID
    return BotMode.RBE

  # For each pool (usually just one) calculate the mode and RBE instance the bot
  # should be using there.
  assert isinstance(pools, list), pools
  per_pool = []  # (BotMode, rbe_instance or None)
  for pool in pools:
    cfg = pools_config.get_pool_config(pool)
    if cfg and cfg.rbe_migration:
      mode = derive_mode(cfg.rbe_migration.bot_mode_allocation)
      per_pool.append((mode, cfg.rbe_migration.rbe_instance))
    else:
      per_pool.append((BotMode.SWARMING, None))

  # If all pools agree on a single mode, use it whatever it is. Otherwise use
  # HYBRID, since it is compatible with all modes.
  modes = list(set(m for m, _ in per_pool))
  if len(modes) == 1:
    mode = modes[0]
  else:
    logging.warning('RBE: bot %s is assigned multiple modes %s', bot_id, modes)
    mode = BotMode.HYBRID
  logging.info('RBE: bot %s is in %s mode', bot_id, mode)

  # Don't bother checking the rest for bots in pure Swarming mode.
  if mode == BotMode.SWARMING:
    return None
  assert mode in (BotMode.HYBRID, BotMode.RBE), mode

  # Check all RBE pools agree on an RBE instance to use. If not, this is a
  # configuration error. Unfortunately it is hard to detect it statically when
  # validating the config. Instead log an error now and pick some arbitrary
  # RBE instance. That way at least some tasks will still be executing.
  rbe_instances = sorted(
      set(inst for m, inst in per_pool if m != BotMode.SWARMING))
  assert rbe_instances
  if len(rbe_instances) > 1:
    logging.error('RBE: bot %s: bot pools disagree on RBE instance: %r', bot_id,
                  rbe_instances)
  rbe_instance = rbe_instances[0]
  logging.info('RBE: bot %s is using RBE instance %s', bot_id, rbe_instance)
  return RBEBotConfig(instance=rbe_instance, hybrid_mode=mode == BotMode.HYBRID)


def get_rbe_instance_for_task(task_tags, pool_cfg):
  """Returns RBE instance to use for a task or None to use native scheduler.

  Args:
    task_tags: a list of string tags (as 'k:v' pairs).
    pool_cfg: pools_config.PoolConfig with the target pool config.

  Returns:
    A string with RBE instance name to use by the bot or None.
  """
  rbe_cfg = pool_cfg.rbe_migration
  if not rbe_cfg or not rbe_cfg.rbe_instance:
    return None

  # Per-task overrides useful for one-off experiments.
  if 'rbe:prevent' in task_tags:
    return None
  if 'rbe:require' in task_tags:
    return rbe_cfg.rbe_instance

  # Random dice.
  if rbe_cfg.rbe_mode_percent <= 0:
    return None
  if rbe_cfg.rbe_mode_percent >= 100:
    return rbe_cfg.rbe_instance
  if random.uniform(0, 100) < rbe_cfg.rbe_mode_percent:
    return rbe_cfg.rbe_instance
  return None


def gen_rbe_reservation_id(task_request_key, task_slice_index):
  """Generates an RBE reservation ID representing a particular slice.

  It needs to globally (potentially across Swarming instances) identify
  a particular task slice. Used to idempotently submit RBE reservations.

  Args:
    task_request_key: a key of the root TaskRequest.
    task_slice_index: the index of the slice to represent.
  """
  assert task_request_key.kind() == 'TaskRequest'
  task_id = task_pack.pack_result_summary_key(
      task_pack.request_key_to_result_summary_key(task_request_key))
  return '%s-%s-%d' % (
      app_identity.get_application_id(),
      task_id,
      task_slice_index,
  )


def enqueue_rbe_task(task_request, task_to_run):
  """Transactionally enqueues a TQ task that eventually submits RBE reservation.

  This is a fire-and-forget operation. If RBE refuses to accept the reservation
  (e.g. fatal errors, no bots available, etc) Swarming will be asynchronously
  notified later.

  Args:
    task_request: an original TaskRequest with all task details.
    task_to_run: a TaskToRunShard representing a single task slice to execute.

  Raises:
    datastore_utils.CommitError if the TQ enqueuing failed.
  """
  assert ndb.in_transaction()
  assert task_request.rbe_instance
  assert task_to_run.rbe_reservation
  assert task_to_run.key.parent() == task_request.key
  assert task_to_run.is_reapable, task_to_run

  # For tracing how long the TQ task is stuck.
  now = timestamp_pb2.Timestamp()
  now.FromDatetime(utils.utcnow())

  # This is always populated for slices with `is_reapable == True`.
  expiry = timestamp_pb2.Timestamp()
  expiry.FromDatetime(task_to_run.expiration_ts)

  # Properties of this particular slice.
  props = task_request.task_slice(task_to_run.task_slice_index).properties

  # Convert dimensions to a format closer to what RBE wants. They are already
  # validated to be correct by that point by _validate_dimensions.
  requested_bot_id = None
  constraints = []
  for k, v in sorted(props.dimensions.items()):
    assert isinstance(v, list), props.dimensions
    if u'id' == k:
      assert len(v) == 1, props.dimensions
      assert OR_DIM_SEP not in v[0], props.dimensions
      requested_bot_id = v[0]
    else:
      # {k: [a, b|c]} => k:a AND (k:b | k:c).
      for alternatives in v:
        constraints.append(
            rbe_pb2.EnqueueRBETask.Constraint(
                key=k,
                allowed_values=alternatives.split(OR_DIM_SEP),
            ))

  # This is format recognized by go.chromium.org/luci/server/tq. It routes
  # based on `class`.
  payload = {
      'class':
      'rbe-enqueue',
      'body':
      json_format.MessageToDict(
          rbe_pb2.EnqueueRBETask(
              payload=rbe_pb2.TaskPayload(
                  reservation_id=task_to_run.rbe_reservation,
                  task_id=task_request.task_id,
                  slice_index=task_to_run.task_slice_index,
                  task_to_run_shard=task_to_run.shard_index,
                  task_to_run_id=task_to_run.key.integer_id(),
                  debug_info=rbe_pb2.TaskPayload.DebugInfo(
                      created=now,
                      py_swarming_version=utils.get_app_version(),
                      task_name=task_request.name,
                  ),
              ),
              rbe_instance=task_request.rbe_instance,
              expiry=expiry,
              requested_bot_id=requested_bot_id,
              constraints=constraints,
              priority=task_request.priority,
              scheduling_algorithm=task_request.scheduling_algorithm,
              execution_timeout=duration_pb2.Duration(
                  seconds=(
                      props.execution_timeout_secs + props.grace_period_secs +
                      30  # some extra to compensate for bot's own overhead
                  ), ),
          )),
  }

  logging.info('RBE: enqueuing task to launch %s', task_to_run.rbe_reservation)
  ok = utils.enqueue_task(
      # The last path components are informational for nicer logs. All data is
      # transferred through `payload`.
      '/internal/tasks/t/rbe-enqueue/%s-%d' % (
          task_request.task_id,
          task_to_run.task_slice_index,
      ),
      'rbe-enqueue',
      transactional=True,
      use_dedicated_module=False,  # let dispatch.yaml decide
      payload=utils.encode_to_json(payload))
  if not ok:
    raise datastore_utils.CommitError('Failed to enqueue RBE reservation')


def enqueue_rbe_cancel(task_request, task_to_run):
  """Transactionally enqueues a TQ task that cancels an RBE reservation.

  Args:
    task_request: an original TaskRequest with all task details.
    task_to_run: a TaskToRunShard representing a reservation to cancel.

  Raises:
    datastore_utils.CommitError if the TQ enqueuing failed.
  """
  assert ndb.in_transaction()
  assert task_request.rbe_instance
  assert task_to_run.rbe_reservation
  assert task_to_run.key.parent() == task_request.key

  # For tracing how long the TQ task is stuck.
  now = timestamp_pb2.Timestamp()
  now.FromDatetime(utils.utcnow())

  # This is format recognized by go.chromium.org/luci/server/tq. It routes
  # based on `class`.
  payload = {
      'class':
      'rbe-cancel',
      'body':
      json_format.MessageToDict(
          rbe_pb2.CancelRBETask(
              rbe_instance=task_request.rbe_instance,
              reservation_id=task_to_run.rbe_reservation,
              debug_info=rbe_pb2.CancelRBETask.DebugInfo(
                  created=now,
                  py_swarming_version=utils.get_app_version(),
                  task_name=task_request.name,
              ),
          ), ),
  }

  logging.info('RBE: enqueuing cancellation %s', task_to_run.rbe_reservation)
  ok = utils.enqueue_task(
      # The last path components are informational for nicer logs. All data is
      # transferred through `payload`.
      '/internal/tasks/t/rbe-cancel/%s-%d' % (
          task_request.task_id,
          task_to_run.task_slice_index,
      ),
      'rbe-cancel',
      transactional=True,
      use_dedicated_module=False,  # let dispatch.yaml decide
      payload=utils.encode_to_json(payload))
  if not ok:
    raise datastore_utils.CommitError('Failed to enqueue RBE cancellation')


### Private stuff.


def _quasi_random_100(s):
  """Given a string, returns a quasi-random integer in range [0; 100)."""
  digest = hashlib.sha256(s).digest()
  num = float(ord(digest[0]) + ord(digest[1]) * 256)
  return int(num * 99.9 / (256.0 + 256.0 * 256.0))
