# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: books.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x62ooks.proto\x12\x04grpc\"\x0e\n\x0c\x42ooksRequest\"*\n\rBooksResponse\x12\x19\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\n.grpc.Book\"*\n\x0e\x41\x64\x64\x42ookRequest\x12\x18\n\x04\x62ook\x18\x01 \x01(\x0b\x32\n.grpc.Book\"+\n\x0f\x41\x64\x64\x42ookResponse\x12\x18\n\x04\x62ook\x18\x01 \x01(\x0b\x32\n.grpc.Book\"1\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t2\x7f\n\x0c\x42ooksService\x12\x35\n\x08GetBooks\x12\x12.grpc.BooksRequest\x1a\x13.grpc.BooksResponse\"\x00\x12\x38\n\x07\x41\x64\x64\x42ook\x12\x14.grpc.AddBookRequest\x1a\x15.grpc.AddBookResponse\"\x00\x42\x13\n\x11org.inf5190.booksb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'books_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021org.inf5190.books'
  _globals['_BOOKSREQUEST']._serialized_start=21
  _globals['_BOOKSREQUEST']._serialized_end=35
  _globals['_BOOKSRESPONSE']._serialized_start=37
  _globals['_BOOKSRESPONSE']._serialized_end=79
  _globals['_ADDBOOKREQUEST']._serialized_start=81
  _globals['_ADDBOOKREQUEST']._serialized_end=123
  _globals['_ADDBOOKRESPONSE']._serialized_start=125
  _globals['_ADDBOOKRESPONSE']._serialized_end=168
  _globals['_BOOK']._serialized_start=170
  _globals['_BOOK']._serialized_end=219
  _globals['_BOOKSSERVICE']._serialized_start=221
  _globals['_BOOKSSERVICE']._serialized_end=348
# @@protoc_insertion_point(module_scope)
