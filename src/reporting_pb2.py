# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reporting.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0freporting.proto\x12\treporting\"\xa0\x03\n\tSpaceship\x12\x31\n\talignment\x18\x04 \x02(\x0e\x32\x1e.reporting.Spaceship.Alignment\x12\x0c\n\x04name\x18\x05 \x02(\t\x12.\n\nship_class\x18\x06 \x02(\x0e\x32\x1a.reporting.Spaceship.Class\x12\x0e\n\x06length\x18\x07 \x02(\x02\x12\x11\n\tcrew_size\x18\x08 \x02(\x05\x12\r\n\x05\x61rmed\x18\t \x02(\x08\x12/\n\x08officers\x18\n \x03(\x0b\x32\x1d.reporting.Spaceship.Officers\x1a?\n\x08Officers\x12\x12\n\nfirst_name\x18\x01 \x02(\t\x12\x11\n\tlast_name\x18\x02 \x02(\t\x12\x0c\n\x04rank\x18\x03 \x02(\t\" \n\tAlignment\x12\x08\n\x04\x41lly\x10\x00\x12\t\n\x05\x45nemy\x10\x01\"\\\n\x05\x43lass\x12\x0c\n\x08\x43orvette\x10\x00\x12\x0b\n\x07\x46rigate\x10\x01\x12\x0b\n\x07\x43ruiser\x10\x02\x12\r\n\tDestroyer\x10\x03\x12\x0b\n\x07\x43\x61rrier\x10\x04\x12\x0f\n\x0b\x44readnought\x10\x05\"Q\n\x0b\x43oordinates\x12\t\n\x01h\x18\x01 \x02(\t\x12\t\n\x01m\x18\x02 \x02(\t\x12\t\n\x01s\x18\x03 \x02(\t\x12\t\n\x01\x64\x18\x04 \x02(\t\x12\n\n\x02\x64m\x18\x05 \x02(\t\x12\n\n\x02\x64s\x18\x06 \x02(\t2P\n\x0fReportingServer\x12=\n\tGetReport\x12\x16.reporting.Coordinates\x1a\x14.reporting.Spaceship\"\x00\x30\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reporting_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SPACESHIP']._serialized_start=31
  _globals['_SPACESHIP']._serialized_end=447
  _globals['_SPACESHIP_OFFICERS']._serialized_start=256
  _globals['_SPACESHIP_OFFICERS']._serialized_end=319
  _globals['_SPACESHIP_ALIGNMENT']._serialized_start=321
  _globals['_SPACESHIP_ALIGNMENT']._serialized_end=353
  _globals['_SPACESHIP_CLASS']._serialized_start=355
  _globals['_SPACESHIP_CLASS']._serialized_end=447
  _globals['_COORDINATES']._serialized_start=449
  _globals['_COORDINATES']._serialized_end=530
  _globals['_REPORTINGSERVER']._serialized_start=532
  _globals['_REPORTINGSERVER']._serialized_end=612
# @@protoc_insertion_point(module_scope)
