# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DataPack.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DataPack.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x44\x61taPack.proto\"\x95\x01\n\x08\x44\x61taPack\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\ttimeStamp\x18\x03 \x01(\x01\x12\x1e\n\nlogin_data\x18\x04 \x01(\x0b\x32\n.LoginData\x12 \n\x0blogout_data\x18\x05 \x01(\x0b\x32\x0b.LogoutData\x12\x1a\n\x08\x61\x63k_data\x18\x06 \x01(\x0b\x32\x08.AckData\"*\n\tLoginData\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"*\n\nLogoutData\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0f\n\x07session\x18\x02 \x01(\t\"@\n\x07\x41\x63kData\x12\x0e\n\x06\x61\x63k_id\x18\x01 \x01(\t\x12\x14\n\x0clogin_status\x18\x02 \x01(\x08\x12\x0f\n\x07session\x18\x03 \x01(\tb\x06proto3'
)




_DATAPACK = _descriptor.Descriptor(
  name='DataPack',
  full_name='DataPack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DataPack.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='DataPack.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='DataPack.timeStamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login_data', full_name='DataPack.login_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logout_data', full_name='DataPack.logout_data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ack_data', full_name='DataPack.ack_data', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=19,
  serialized_end=168,
)


_LOGINDATA = _descriptor.Descriptor(
  name='LoginData',
  full_name='LoginData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='LoginData.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='LoginData.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=170,
  serialized_end=212,
)


_LOGOUTDATA = _descriptor.Descriptor(
  name='LogoutData',
  full_name='LogoutData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='LogoutData.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session', full_name='LogoutData.session', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=214,
  serialized_end=256,
)


_ACKDATA = _descriptor.Descriptor(
  name='AckData',
  full_name='AckData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack_id', full_name='AckData.ack_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login_status', full_name='AckData.login_status', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session', full_name='AckData.session', index=2,
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
  serialized_start=258,
  serialized_end=322,
)

_DATAPACK.fields_by_name['login_data'].message_type = _LOGINDATA
_DATAPACK.fields_by_name['logout_data'].message_type = _LOGOUTDATA
_DATAPACK.fields_by_name['ack_data'].message_type = _ACKDATA
DESCRIPTOR.message_types_by_name['DataPack'] = _DATAPACK
DESCRIPTOR.message_types_by_name['LoginData'] = _LOGINDATA
DESCRIPTOR.message_types_by_name['LogoutData'] = _LOGOUTDATA
DESCRIPTOR.message_types_by_name['AckData'] = _ACKDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataPack = _reflection.GeneratedProtocolMessageType('DataPack', (_message.Message,), {
  'DESCRIPTOR' : _DATAPACK,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:DataPack)
  })
_sym_db.RegisterMessage(DataPack)

LoginData = _reflection.GeneratedProtocolMessageType('LoginData', (_message.Message,), {
  'DESCRIPTOR' : _LOGINDATA,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:LoginData)
  })
_sym_db.RegisterMessage(LoginData)

LogoutData = _reflection.GeneratedProtocolMessageType('LogoutData', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTDATA,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:LogoutData)
  })
_sym_db.RegisterMessage(LogoutData)

AckData = _reflection.GeneratedProtocolMessageType('AckData', (_message.Message,), {
  'DESCRIPTOR' : _ACKDATA,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:AckData)
  })
_sym_db.RegisterMessage(AckData)


# @@protoc_insertion_point(module_scope)
