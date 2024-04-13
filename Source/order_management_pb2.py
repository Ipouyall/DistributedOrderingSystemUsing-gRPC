# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order_management.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16order_management.proto\x12\x0fordermanagement\"\"\n\x0cOrderRequest\x12\x12\n\norder_name\x18\x01 \x01(\t\"5\n\rOrderResponse\x12\x11\n\titem_name\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\".\n\x16ReceiveMessagesRequest\x12\x14\n\x0cnum_messages\x18\x01 \x01(\x05\"+\n\x17ReceiveMessagesResponse\x12\x10\n\x08messages\x18\x01 \x03(\t\")\n\x15UploadMessagesRequest\x12\x10\n\x08messages\x18\x01 \x03(\t\".\n\x16UploadMessagesResponse\x12\x14\n\x0c\x63onfirmation\x18\x01 \x01(\t\"\x1e\n\x0b\x43hatMessage\x12\x0f\n\x07message\x18\x01 \x01(\t2\xfd\x02\n\x0fOrderManagement\x12K\n\x08getOrder\x12\x1d.ordermanagement.OrderRequest\x1a\x1e.ordermanagement.OrderResponse\"\x00\x12\x65\n\x0csearchOrders\x12\'.ordermanagement.ReceiveMessagesRequest\x1a(.ordermanagement.ReceiveMessagesResponse\"\x00\x30\x01\x12\x63\n\x0cupdateOrders\x12&.ordermanagement.UploadMessagesRequest\x1a\'.ordermanagement.UploadMessagesResponse\"\x00(\x01\x12Q\n\rprocessOrders\x12\x1c.ordermanagement.ChatMessage\x1a\x1c.ordermanagement.ChatMessage\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_management_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ORDERREQUEST']._serialized_start=43
  _globals['_ORDERREQUEST']._serialized_end=77
  _globals['_ORDERRESPONSE']._serialized_start=79
  _globals['_ORDERRESPONSE']._serialized_end=132
  _globals['_RECEIVEMESSAGESREQUEST']._serialized_start=134
  _globals['_RECEIVEMESSAGESREQUEST']._serialized_end=180
  _globals['_RECEIVEMESSAGESRESPONSE']._serialized_start=182
  _globals['_RECEIVEMESSAGESRESPONSE']._serialized_end=225
  _globals['_UPLOADMESSAGESREQUEST']._serialized_start=227
  _globals['_UPLOADMESSAGESREQUEST']._serialized_end=268
  _globals['_UPLOADMESSAGESRESPONSE']._serialized_start=270
  _globals['_UPLOADMESSAGESRESPONSE']._serialized_end=316
  _globals['_CHATMESSAGE']._serialized_start=318
  _globals['_CHATMESSAGE']._serialized_end=348
  _globals['_ORDERMANAGEMENT']._serialized_start=351
  _globals['_ORDERMANAGEMENT']._serialized_end=732
# @@protoc_insertion_point(module_scope)
