# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: activity.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='activity.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x61\x63tivity.proto\"\xe5\x03\n\x08\x41\x63tivity\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x11\n\tplayer_id\x18\x02 \x02(\x04\x12\n\n\x02\x66\x33\x18\x03 \x02(\r\x12\x0c\n\x04name\x18\x04 \x02(\t\x12\n\n\x02\x66\x35\x18\x05 \x01(\r\x12\n\n\x02\x66\x36\x18\x06 \x01(\r\x12\x12\n\nstart_date\x18\x07 \x02(\t\x12\x10\n\x08\x65nd_date\x18\x08 \x01(\t\x12\x10\n\x08\x64istance\x18\t \x01(\x02\x12\x16\n\x0e\x61vg_heart_rate\x18\n \x01(\x02\x12\x16\n\x0emax_heart_rate\x18\x0b \x01(\x02\x12\x11\n\tavg_watts\x18\x0c \x01(\x02\x12\x11\n\tmax_watts\x18\r \x01(\x02\x12\x13\n\x0b\x61vg_cadence\x18\x0e \x01(\x02\x12\x13\n\x0bmax_cadence\x18\x0f \x01(\x02\x12\x11\n\tavg_speed\x18\x10 \x01(\x02\x12\x11\n\tmax_speed\x18\x11 \x01(\x02\x12\x10\n\x08\x63\x61lories\x18\x12 \x01(\x02\x12\x17\n\x0ftotal_elevation\x18\x13 \x01(\x02\x12\x18\n\x10strava_upload_id\x18\x14 \x01(\x04\x12\x1a\n\x12strava_activity_id\x18\x15 \x01(\x04\x12\x0b\n\x03\x66\x32\x33\x18\x17 \x01(\r\x12\x0b\n\x03\x66it\x18\x18 \x01(\x0c\x12\x14\n\x0c\x66it_filename\x18\x19 \x01(\t\x12\x0b\n\x03\x66\x32\x39\x18\x1d \x01(\r\x12\x0c\n\x04\x64\x61te\x18\x1f \x01(\t\"+\n\nActivities\x12\x1d\n\nactivities\x18\x01 \x03(\x0b\x32\t.Activity'
)




_ACTIVITY = _descriptor.Descriptor(
  name='Activity',
  full_name='Activity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Activity.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='Activity.player_id', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f3', full_name='Activity.f3', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Activity.name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f5', full_name='Activity.f5', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f6', full_name='Activity.f6', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='Activity.start_date', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='Activity.end_date', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='Activity.distance', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_heart_rate', full_name='Activity.avg_heart_rate', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_heart_rate', full_name='Activity.max_heart_rate', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_watts', full_name='Activity.avg_watts', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_watts', full_name='Activity.max_watts', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_cadence', full_name='Activity.avg_cadence', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_cadence', full_name='Activity.max_cadence', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_speed', full_name='Activity.avg_speed', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_speed', full_name='Activity.max_speed', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calories', full_name='Activity.calories', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_elevation', full_name='Activity.total_elevation', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strava_upload_id', full_name='Activity.strava_upload_id', index=19,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strava_activity_id', full_name='Activity.strava_activity_id', index=20,
      number=21, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f23', full_name='Activity.f23', index=21,
      number=23, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fit', full_name='Activity.fit', index=22,
      number=24, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fit_filename', full_name='Activity.fit_filename', index=23,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f29', full_name='Activity.f29', index=24,
      number=29, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='Activity.date', index=25,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=504,
)


_ACTIVITIES = _descriptor.Descriptor(
  name='Activities',
  full_name='Activities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activities', full_name='Activities.activities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=549,
)

_ACTIVITIES.fields_by_name['activities'].message_type = _ACTIVITY
DESCRIPTOR.message_types_by_name['Activity'] = _ACTIVITY
DESCRIPTOR.message_types_by_name['Activities'] = _ACTIVITIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Activity = _reflection.GeneratedProtocolMessageType('Activity', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITY,
  '__module__' : 'activity_pb2'
  # @@protoc_insertion_point(class_scope:Activity)
  })
_sym_db.RegisterMessage(Activity)

Activities = _reflection.GeneratedProtocolMessageType('Activities', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITIES,
  '__module__' : 'activity_pb2'
  # @@protoc_insertion_point(class_scope:Activities)
  })
_sym_db.RegisterMessage(Activities)


# @@protoc_insertion_point(module_scope)
