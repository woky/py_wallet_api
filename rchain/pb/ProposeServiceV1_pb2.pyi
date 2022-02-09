"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import ServiceError_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ProposeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> ServiceError_pb2.ServiceError: ...
    result: typing.Text
    def __init__(self,
        *,
        error: typing.Optional[ServiceError_pb2.ServiceError] = ...,
        result: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","message",b"message","result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","message",b"message","result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message",b"message"]) -> typing.Optional[typing_extensions.Literal["error","result"]]: ...
global___ProposeResponse = ProposeResponse

class ProposeResultResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def error(self) -> ServiceError_pb2.ServiceError: ...
    result: typing.Text
    def __init__(self,
        *,
        error: typing.Optional[ServiceError_pb2.ServiceError] = ...,
        result: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["error",b"error","message",b"message","result",b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error","message",b"message","result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message",b"message"]) -> typing.Optional[typing_extensions.Literal["error","result"]]: ...
global___ProposeResultResponse = ProposeResultResponse
