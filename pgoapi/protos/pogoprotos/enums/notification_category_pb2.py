# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/notification_category.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/notification_category.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/enums/notification_category.proto\x12\x10pogoprotos.enums*\xa8\x01\n\x14NotificationCategory\x12\x1e\n\x1aUNSET_NotificationCategory\x10\x00\x12\x0f\n\x0bGYM_REMOVAL\x10\x01\x12\x12\n\x0ePOKEMON_HUNGRY\x10\x02\x12\x0f\n\x0bPOKEMON_WON\x10\x03\x12\x19\n\x15\x45XCLUSIVE_RAID_INVITE\x10\x04\x12\x1f\n\x1b\x45XCLUSIVE_RAID_CANCELLATION\x10\x05\x62\x06proto3')
)

_NOTIFICATIONCATEGORY = _descriptor.EnumDescriptor(
  name='NotificationCategory',
  full_name='pogoprotos.enums.NotificationCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_NotificationCategory', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_REMOVAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_HUNGRY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_WON', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_INVITE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_CANCELLATION', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=67,
  serialized_end=235,
)
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONCATEGORY)

NotificationCategory = enum_type_wrapper.EnumTypeWrapper(_NOTIFICATIONCATEGORY)
UNSET_NotificationCategory = 0
GYM_REMOVAL = 1
POKEMON_HUNGRY = 2
POKEMON_WON = 3
EXCLUSIVE_RAID_INVITE = 4
EXCLUSIVE_RAID_CANCELLATION = 5


DESCRIPTOR.enum_types_by_name['NotificationCategory'] = _NOTIFICATIONCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
