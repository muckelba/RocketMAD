# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/login_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/login_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/settings/login_settings.proto\x12\x13pogoprotos.settings\"3\n\rLoginSettings\x12\"\n\x1a\x65nable_multi_login_linking\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOGINSETTINGS = _descriptor.Descriptor(
  name='LoginSettings',
  full_name='pogoprotos.settings.LoginSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_multi_login_linking', full_name='pogoprotos.settings.LoginSettings.enable_multi_login_linking', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=116,
)

DESCRIPTOR.message_types_by_name['LoginSettings'] = _LOGINSETTINGS

LoginSettings = _reflection.GeneratedProtocolMessageType('LoginSettings', (_message.Message,), dict(
  DESCRIPTOR = _LOGINSETTINGS,
  __module__ = 'pogoprotos.settings.login_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.LoginSettings)
  ))
_sym_db.RegisterMessage(LoginSettings)


# @@protoc_insertion_point(module_scope)
