# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class ServiceError(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    messages = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        messages : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> ServiceError: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"messages"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"messages",b"messages"]) -> None: ...
