# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProposeService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CasperMessage_pb2 as CasperMessage__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import Either_pb2 as Either__pb2
from scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProposeService.proto',
  package='coop.rchain.casper.protocol',
  syntax='proto3',
  serialized_options=_b('\342?!\n\033coop.rchain.casper.protocol\020\001(\001'),
  serialized_pb=_b('\n\x14ProposeService.proto\x12\x1b\x63oop.rchain.casper.protocol\x1a\x13\x43\x61sperMessage.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0c\x45ither.proto\x1a\x15scalapb/scalapb.proto2>\n\x0eProposeService\x12,\n\x07propose\x12\x16.google.protobuf.Empty\x1a\x07.Either\"\x00\x42$\xe2?!\n\x1b\x63oop.rchain.casper.protocol\x10\x01(\x01\x62\x06proto3')
  ,
  dependencies=[CasperMessage__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,Either__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PROPOSESERVICE = _descriptor.ServiceDescriptor(
  name='ProposeService',
  full_name='coop.rchain.casper.protocol.ProposeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=140,
  serialized_end=202,
  methods=[
  _descriptor.MethodDescriptor(
    name='propose',
    full_name='coop.rchain.casper.protocol.ProposeService.propose',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=Either__pb2._EITHER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROPOSESERVICE)

DESCRIPTOR.services_by_name['ProposeService'] = _PROPOSESERVICE

# @@protoc_insertion_point(module_scope)
