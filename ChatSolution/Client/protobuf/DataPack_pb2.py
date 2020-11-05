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
  serialized_pb=b'\n\x0e\x44\x61taPack.proto\"\xcc\x02\n\x08\x44\x61taPack\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\ttimeStamp\x18\x03 \x01(\x01\x12\x1e\n\nlogin_data\x18\x04 \x01(\x0b\x32\n.LoginData\x12 \n\x0blogout_data\x18\x05 \x01(\x0b\x32\x0b.LogoutData\x12\x1a\n\x08\x61\x63k_data\x18\x06 \x01(\x0b\x32\x08.AckData\x12\x1c\n\tuser_info\x18\x07 \x01(\x0b\x32\t.UserInfo\x12\x15\n\x07one_msg\x18\x08 \x01(\x0b\x32\x04.Msg\x12#\n\x0bget_msg_req\x18\t \x01(\x0b\x32\x0e.ReqHistoryMsg\x12\x1f\n\x0c\x66riends_info\x18\n \x03(\x0b\x32\t.UserInfo\x12\x1f\n\x0bgroups_info\x18\x0b \x03(\x0b\x32\n.GroupInfo\x12\x19\n\x0boffline_msg\x18\x0c \x03(\x0b\x32\x04.Msg\"*\n\tLoginData\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"*\n\nLogoutData\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0f\n\x07session\x18\x02 \x01(\t\"@\n\x07\x41\x63kData\x12\x0e\n\x06\x61\x63k_id\x18\x01 \x01(\t\x12\x14\n\x0clogin_status\x18\x02 \x01(\x08\x12\x0f\n\x07session\x18\x03 \x01(\t\"y\n\x08UserInfo\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x11\n\tnick_name\x18\x02 \x01(\t\x12\x0e\n\x06isMale\x18\x03 \x01(\x08\x12\x19\n\x11registration_time\x18\x04 \x01(\x01\x12\x12\n\nstart_time\x18\x05 \x01(\x01\x12\x0e\n\x06\x61vatar\x18\x06 \x01(\x0c\"S\n\tGroupInfo\x12\x0c\n\x04g_id\x18\x01 \x01(\t\x12\x0e\n\x06g_name\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\t\x12\x14\n\x0cgroup_member\x18\x04 \x03(\t\"T\n\x03Msg\x12\x0f\n\x07\x66rom_id\x18\x01 \x01(\t\x12\r\n\x05to_id\x18\x02 \x01(\t\x12\x10\n\x08msg_type\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\r\n\x05image\x18\x05 \x01(\x0c\">\n\rReqHistoryMsg\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x12\n\nanother_id\x18\x03 \x01(\tb\x06proto3'
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
    _descriptor.FieldDescriptor(
      name='user_info', full_name='DataPack.user_info', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='one_msg', full_name='DataPack.one_msg', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_msg_req', full_name='DataPack.get_msg_req', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='friends_info', full_name='DataPack.friends_info', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groups_info', full_name='DataPack.groups_info', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offline_msg', full_name='DataPack.offline_msg', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=351,
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
  serialized_start=353,
  serialized_end=395,
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
  serialized_start=397,
  serialized_end=439,
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
  serialized_start=441,
  serialized_end=505,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='UserInfo.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nick_name', full_name='UserInfo.nick_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isMale', full_name='UserInfo.isMale', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registration_time', full_name='UserInfo.registration_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='UserInfo.start_time', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='UserInfo.avatar', index=5,
      number=6, type=12, cpp_type=9, label=1,
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
  serialized_start=507,
  serialized_end=628,
)


_GROUPINFO = _descriptor.Descriptor(
  name='GroupInfo',
  full_name='GroupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='g_id', full_name='GroupInfo.g_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='g_name', full_name='GroupInfo.g_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='GroupInfo.start_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_member', full_name='GroupInfo.group_member', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=630,
  serialized_end=713,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_id', full_name='Msg.from_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_id', full_name='Msg.to_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='Msg.msg_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='Msg.text', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='Msg.image', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=715,
  serialized_end=799,
)


_REQHISTORYMSG = _descriptor.Descriptor(
  name='ReqHistoryMsg',
  full_name='ReqHistoryMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='ReqHistoryMsg.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ReqHistoryMsg.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='another_id', full_name='ReqHistoryMsg.another_id', index=2,
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
  serialized_start=801,
  serialized_end=863,
)

_DATAPACK.fields_by_name['login_data'].message_type = _LOGINDATA
_DATAPACK.fields_by_name['logout_data'].message_type = _LOGOUTDATA
_DATAPACK.fields_by_name['ack_data'].message_type = _ACKDATA
_DATAPACK.fields_by_name['user_info'].message_type = _USERINFO
_DATAPACK.fields_by_name['one_msg'].message_type = _MSG
_DATAPACK.fields_by_name['get_msg_req'].message_type = _REQHISTORYMSG
_DATAPACK.fields_by_name['friends_info'].message_type = _USERINFO
_DATAPACK.fields_by_name['groups_info'].message_type = _GROUPINFO
_DATAPACK.fields_by_name['offline_msg'].message_type = _MSG
DESCRIPTOR.message_types_by_name['DataPack'] = _DATAPACK
DESCRIPTOR.message_types_by_name['LoginData'] = _LOGINDATA
DESCRIPTOR.message_types_by_name['LogoutData'] = _LOGOUTDATA
DESCRIPTOR.message_types_by_name['AckData'] = _ACKDATA
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['GroupInfo'] = _GROUPINFO
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['ReqHistoryMsg'] = _REQHISTORYMSG
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

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

GroupInfo = _reflection.GeneratedProtocolMessageType('GroupInfo', (_message.Message,), {
  'DESCRIPTOR' : _GROUPINFO,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:GroupInfo)
  })
_sym_db.RegisterMessage(GroupInfo)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:Msg)
  })
_sym_db.RegisterMessage(Msg)

ReqHistoryMsg = _reflection.GeneratedProtocolMessageType('ReqHistoryMsg', (_message.Message,), {
  'DESCRIPTOR' : _REQHISTORYMSG,
  '__module__' : 'DataPack_pb2'
  # @@protoc_insertion_point(class_scope:ReqHistoryMsg)
  })
_sym_db.RegisterMessage(ReqHistoryMsg)


# @@protoc_insertion_point(module_scope)
