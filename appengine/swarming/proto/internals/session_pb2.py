# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/internals/session.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from proto.config import bots_pb2 as proto_dot_config_dot_bots__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/internals/session.proto',
  package='swarming.internals.session',
  syntax='proto3',
  serialized_options=b'Z9go.chromium.org/luci/swarming/proto/internals;internalspb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dproto/internals/session.proto\x12\x1aswarming.internals.session\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17proto/config/bots.proto\"\x8e\x02\n\x0cSessionToken\x12J\n\x0bhmac_tagged\x18\x01 \x01(\x0b\x32\x33.swarming.internals.session.SessionToken.HmacTaggedH\x00\x12P\n\x0e\x61\x65\x61\x64_encrypted\x18\x02 \x01(\x0b\x32\x36.swarming.internals.session.SessionToken.AeadEncryptedH\x00\x1a\x32\n\nHmacTagged\x12\x0f\n\x07session\x18\x01 \x01(\x0c\x12\x13\n\x0bhmac_sha256\x18\x02 \x01(\x0c\x1a$\n\rAeadEncrypted\x12\x13\n\x0b\x63ipher_text\x18\x01 \x01(\x0c\x42\x06\n\x04kind\"\xc2\x02\n\x07Session\x12\x0e\n\x06\x62ot_id\x18\x01 \x01(\t\x12\x14\n\x0csession_name\x18\x02 \x01(\t\x12*\n\x06\x65xpiry\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\ndebug_info\x18\x04 \x01(\x0b\x32%.swarming.internals.session.DebugInfo\x12\x39\n\nbot_config\x18\x05 \x01(\x0b\x32%.swarming.internals.session.BotConfig\x12\x1d\n\x15handshake_config_hash\x18\x06 \x01(\x0c\x12\x1a\n\x12rbe_bot_session_id\x18\x07 \x01(\t\x12\x34\n\x10last_seen_config\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf0\x01\n\tBotConfig\x12*\n\x06\x65xpiry\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\ndebug_info\x18\x02 \x01(\x0b\x32%.swarming.internals.session.DebugInfo\x12*\n\x08\x62ot_auth\x18\x03 \x01(\x0b\x32\x18.swarming.config.BotAuth\x12\x1e\n\x16system_service_account\x18\x04 \x01(\t\x12\x1a\n\x12logs_cloud_project\x18\x05 \x01(\t\x12\x14\n\x0crbe_instance\x18\x06 \x01(\t\"f\n\tDebugInfo\x12+\n\x07\x63reated\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10swarming_version\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\tB;Z9go.chromium.org/luci/swarming/proto/internals;internalspbb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,proto_dot_config_dot_bots__pb2.DESCRIPTOR,])




_SESSIONTOKEN_HMACTAGGED = _descriptor.Descriptor(
  name='HmacTagged',
  full_name='swarming.internals.session.SessionToken.HmacTagged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='swarming.internals.session.SessionToken.HmacTagged.session', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hmac_sha256', full_name='swarming.internals.session.SessionToken.HmacTagged.hmac_sha256', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=344,
)

_SESSIONTOKEN_AEADENCRYPTED = _descriptor.Descriptor(
  name='AeadEncrypted',
  full_name='swarming.internals.session.SessionToken.AeadEncrypted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cipher_text', full_name='swarming.internals.session.SessionToken.AeadEncrypted.cipher_text', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=382,
)

_SESSIONTOKEN = _descriptor.Descriptor(
  name='SessionToken',
  full_name='swarming.internals.session.SessionToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hmac_tagged', full_name='swarming.internals.session.SessionToken.hmac_tagged', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aead_encrypted', full_name='swarming.internals.session.SessionToken.aead_encrypted', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SESSIONTOKEN_HMACTAGGED, _SESSIONTOKEN_AEADENCRYPTED, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='swarming.internals.session.SessionToken.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=120,
  serialized_end=390,
)


_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='swarming.internals.session.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bot_id', full_name='swarming.internals.session.Session.bot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_name', full_name='swarming.internals.session.Session.session_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='swarming.internals.session.Session.expiry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug_info', full_name='swarming.internals.session.Session.debug_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_config', full_name='swarming.internals.session.Session.bot_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='handshake_config_hash', full_name='swarming.internals.session.Session.handshake_config_hash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rbe_bot_session_id', full_name='swarming.internals.session.Session.rbe_bot_session_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_seen_config', full_name='swarming.internals.session.Session.last_seen_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=715,
)


_BOTCONFIG = _descriptor.Descriptor(
  name='BotConfig',
  full_name='swarming.internals.session.BotConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='expiry', full_name='swarming.internals.session.BotConfig.expiry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug_info', full_name='swarming.internals.session.BotConfig.debug_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_auth', full_name='swarming.internals.session.BotConfig.bot_auth', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system_service_account', full_name='swarming.internals.session.BotConfig.system_service_account', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs_cloud_project', full_name='swarming.internals.session.BotConfig.logs_cloud_project', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rbe_instance', full_name='swarming.internals.session.BotConfig.rbe_instance', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=958,
)


_DEBUGINFO = _descriptor.Descriptor(
  name='DebugInfo',
  full_name='swarming.internals.session.DebugInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='swarming.internals.session.DebugInfo.created', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='swarming_version', full_name='swarming.internals.session.DebugInfo.swarming_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='swarming.internals.session.DebugInfo.request_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=960,
  serialized_end=1062,
)

_SESSIONTOKEN_HMACTAGGED.containing_type = _SESSIONTOKEN
_SESSIONTOKEN_AEADENCRYPTED.containing_type = _SESSIONTOKEN
_SESSIONTOKEN.fields_by_name['hmac_tagged'].message_type = _SESSIONTOKEN_HMACTAGGED
_SESSIONTOKEN.fields_by_name['aead_encrypted'].message_type = _SESSIONTOKEN_AEADENCRYPTED
_SESSIONTOKEN.oneofs_by_name['kind'].fields.append(
  _SESSIONTOKEN.fields_by_name['hmac_tagged'])
_SESSIONTOKEN.fields_by_name['hmac_tagged'].containing_oneof = _SESSIONTOKEN.oneofs_by_name['kind']
_SESSIONTOKEN.oneofs_by_name['kind'].fields.append(
  _SESSIONTOKEN.fields_by_name['aead_encrypted'])
_SESSIONTOKEN.fields_by_name['aead_encrypted'].containing_oneof = _SESSIONTOKEN.oneofs_by_name['kind']
_SESSION.fields_by_name['expiry'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SESSION.fields_by_name['debug_info'].message_type = _DEBUGINFO
_SESSION.fields_by_name['bot_config'].message_type = _BOTCONFIG
_SESSION.fields_by_name['last_seen_config'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOTCONFIG.fields_by_name['expiry'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BOTCONFIG.fields_by_name['debug_info'].message_type = _DEBUGINFO
_BOTCONFIG.fields_by_name['bot_auth'].message_type = proto_dot_config_dot_bots__pb2._BOTAUTH
_DEBUGINFO.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['SessionToken'] = _SESSIONTOKEN
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['BotConfig'] = _BOTCONFIG
DESCRIPTOR.message_types_by_name['DebugInfo'] = _DEBUGINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionToken = _reflection.GeneratedProtocolMessageType('SessionToken', (_message.Message,), {

  'HmacTagged' : _reflection.GeneratedProtocolMessageType('HmacTagged', (_message.Message,), {
    'DESCRIPTOR' : _SESSIONTOKEN_HMACTAGGED,
    '__module__' : 'proto.internals.session_pb2'
    # @@protoc_insertion_point(class_scope:swarming.internals.session.SessionToken.HmacTagged)
    })
  ,

  'AeadEncrypted' : _reflection.GeneratedProtocolMessageType('AeadEncrypted', (_message.Message,), {
    'DESCRIPTOR' : _SESSIONTOKEN_AEADENCRYPTED,
    '__module__' : 'proto.internals.session_pb2'
    # @@protoc_insertion_point(class_scope:swarming.internals.session.SessionToken.AeadEncrypted)
    })
  ,
  'DESCRIPTOR' : _SESSIONTOKEN,
  '__module__' : 'proto.internals.session_pb2'
  # @@protoc_insertion_point(class_scope:swarming.internals.session.SessionToken)
  })
_sym_db.RegisterMessage(SessionToken)
_sym_db.RegisterMessage(SessionToken.HmacTagged)
_sym_db.RegisterMessage(SessionToken.AeadEncrypted)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'proto.internals.session_pb2'
  # @@protoc_insertion_point(class_scope:swarming.internals.session.Session)
  })
_sym_db.RegisterMessage(Session)

BotConfig = _reflection.GeneratedProtocolMessageType('BotConfig', (_message.Message,), {
  'DESCRIPTOR' : _BOTCONFIG,
  '__module__' : 'proto.internals.session_pb2'
  # @@protoc_insertion_point(class_scope:swarming.internals.session.BotConfig)
  })
_sym_db.RegisterMessage(BotConfig)

DebugInfo = _reflection.GeneratedProtocolMessageType('DebugInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGINFO,
  '__module__' : 'proto.internals.session_pb2'
  # @@protoc_insertion_point(class_scope:swarming.internals.session.DebugInfo)
  })
_sym_db.RegisterMessage(DebugInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
