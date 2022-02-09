"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Node(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    TCP_PORT_FIELD_NUMBER: builtins.int
    UDP_PORT_FIELD_NUMBER: builtins.int
    id: builtins.bytes
    host: builtins.bytes
    tcp_port: builtins.int
    udp_port: builtins.int
    def __init__(self,
        *,
        id: builtins.bytes = ...,
        host: builtins.bytes = ...,
        tcp_port: builtins.int = ...,
        udp_port: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host",b"host","id",b"id","tcp_port",b"tcp_port","udp_port",b"udp_port"]) -> None: ...
global___Node = Node

class Header(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SENDER_FIELD_NUMBER: builtins.int
    NETWORKID_FIELD_NUMBER: builtins.int
    @property
    def sender(self) -> global___Node: ...
    networkId: typing.Text
    def __init__(self,
        *,
        sender: typing.Optional[global___Node] = ...,
        networkId: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sender",b"sender"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["networkId",b"networkId","sender",b"sender"]) -> None: ...
global___Header = Header

class Heartbeat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___Heartbeat = Heartbeat

class HeartbeatResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___HeartbeatResponse = HeartbeatResponse

class ProtocolHandshake(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NONCE_FIELD_NUMBER: builtins.int
    nonce: builtins.bytes
    def __init__(self,
        *,
        nonce: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nonce",b"nonce"]) -> None: ...
global___ProtocolHandshake = ProtocolHandshake

class ProtocolHandshakeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NONCE_FIELD_NUMBER: builtins.int
    nonce: builtins.bytes
    def __init__(self,
        *,
        nonce: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nonce",b"nonce"]) -> None: ...
global___ProtocolHandshakeResponse = ProtocolHandshakeResponse

class Packet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPEID_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    typeId: typing.Text
    content: builtins.bytes
    def __init__(self,
        *,
        typeId: typing.Text = ...,
        content: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","typeId",b"typeId"]) -> None: ...
global___Packet = Packet

class Disconnect(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___Disconnect = Disconnect

class Protocol(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    HEARTBEAT_FIELD_NUMBER: builtins.int
    PROTOCOL_HANDSHAKE_FIELD_NUMBER: builtins.int
    PROTOCOL_HANDSHAKE_RESPONSE_FIELD_NUMBER: builtins.int
    PACKET_FIELD_NUMBER: builtins.int
    DISCONNECT_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___Header: ...
    @property
    def heartbeat(self) -> global___Heartbeat: ...
    @property
    def protocol_handshake(self) -> global___ProtocolHandshake: ...
    @property
    def protocol_handshake_response(self) -> global___ProtocolHandshakeResponse: ...
    @property
    def packet(self) -> global___Packet: ...
    @property
    def disconnect(self) -> global___Disconnect: ...
    def __init__(self,
        *,
        header: typing.Optional[global___Header] = ...,
        heartbeat: typing.Optional[global___Heartbeat] = ...,
        protocol_handshake: typing.Optional[global___ProtocolHandshake] = ...,
        protocol_handshake_response: typing.Optional[global___ProtocolHandshakeResponse] = ...,
        packet: typing.Optional[global___Packet] = ...,
        disconnect: typing.Optional[global___Disconnect] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["disconnect",b"disconnect","header",b"header","heartbeat",b"heartbeat","message",b"message","packet",b"packet","protocol_handshake",b"protocol_handshake","protocol_handshake_response",b"protocol_handshake_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["disconnect",b"disconnect","header",b"header","heartbeat",b"heartbeat","message",b"message","packet",b"packet","protocol_handshake",b"protocol_handshake","protocol_handshake_response",b"protocol_handshake_response"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message",b"message"]) -> typing.Optional[typing_extensions.Literal["heartbeat","protocol_handshake","protocol_handshake_response","packet","disconnect"]]: ...
global___Protocol = Protocol

class TLRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROTOCOL_FIELD_NUMBER: builtins.int
    @property
    def protocol(self) -> global___Protocol: ...
    def __init__(self,
        *,
        protocol: typing.Optional[global___Protocol] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["protocol",b"protocol"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["protocol",b"protocol"]) -> None: ...
global___TLRequest = TLRequest

class InternalServerError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_FIELD_NUMBER: builtins.int
    error: builtins.bytes
    def __init__(self,
        *,
        error: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error",b"error"]) -> None: ...
global___InternalServerError = InternalServerError

class Ack(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___Header: ...
    def __init__(self,
        *,
        header: typing.Optional[global___Header] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["header",b"header"]) -> None: ...
global___Ack = Ack

class TLResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACK_FIELD_NUMBER: builtins.int
    INTERNALSERVERERROR_FIELD_NUMBER: builtins.int
    @property
    def ack(self) -> global___Ack: ...
    @property
    def internalServerError(self) -> global___InternalServerError: ...
    def __init__(self,
        *,
        ack: typing.Optional[global___Ack] = ...,
        internalServerError: typing.Optional[global___InternalServerError] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["ack",b"ack","internalServerError",b"internalServerError","payload",b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ack",b"ack","internalServerError",b"internalServerError","payload",b"payload"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["payload",b"payload"]) -> typing.Optional[typing_extensions.Literal["ack","internalServerError"]]: ...
global___TLResponse = TLResponse

class ChunkHeader(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SENDER_FIELD_NUMBER: builtins.int
    TYPEID_FIELD_NUMBER: builtins.int
    COMPRESSED_FIELD_NUMBER: builtins.int
    CONTENTLENGTH_FIELD_NUMBER: builtins.int
    NETWORKID_FIELD_NUMBER: builtins.int
    @property
    def sender(self) -> global___Node: ...
    typeId: typing.Text
    compressed: builtins.bool
    contentLength: builtins.int
    networkId: typing.Text
    def __init__(self,
        *,
        sender: typing.Optional[global___Node] = ...,
        typeId: typing.Text = ...,
        compressed: builtins.bool = ...,
        contentLength: builtins.int = ...,
        networkId: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["sender",b"sender"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compressed",b"compressed","contentLength",b"contentLength","networkId",b"networkId","sender",b"sender","typeId",b"typeId"]) -> None: ...
global___ChunkHeader = ChunkHeader

class ChunkData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTENTDATA_FIELD_NUMBER: builtins.int
    contentData: builtins.bytes
    def __init__(self,
        *,
        contentData: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["contentData",b"contentData"]) -> None: ...
global___ChunkData = ChunkData

class Chunk(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HEADER_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def header(self) -> global___ChunkHeader: ...
    @property
    def data(self) -> global___ChunkData: ...
    def __init__(self,
        *,
        header: typing.Optional[global___ChunkHeader] = ...,
        data: typing.Optional[global___ChunkData] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content",b"content","data",b"data","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["content",b"content","data",b"data","header",b"header"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["content",b"content"]) -> typing.Optional[typing_extensions.Literal["header","data"]]: ...
global___Chunk = Chunk
