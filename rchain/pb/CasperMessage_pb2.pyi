"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import RhoTypes_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class HasBlockRequestProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HASH_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    def __init__(self,
        *,
        hash: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash",b"hash"]) -> None: ...
global___HasBlockRequestProto = HasBlockRequestProto

class HasBlockProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HASH_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    def __init__(self,
        *,
        hash: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash",b"hash"]) -> None: ...
global___HasBlockProto = HasBlockProto

class BlockRequestProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HASH_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    def __init__(self,
        *,
        hash: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash",b"hash"]) -> None: ...
global___BlockRequestProto = BlockRequestProto

class ForkChoiceTipRequestProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___ForkChoiceTipRequestProto = ForkChoiceTipRequestProto

class ApprovedBlockCandidateProto(google.protobuf.message.Message):
    """---------- Signing Protocol ---------"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BLOCK_FIELD_NUMBER: builtins.int
    REQUIREDSIGS_FIELD_NUMBER: builtins.int
    @property
    def block(self) -> global___BlockMessageProto: ...
    requiredSigs: builtins.int
    def __init__(self,
        *,
        block: typing.Optional[global___BlockMessageProto] = ...,
        requiredSigs: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block",b"block"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block",b"block","requiredSigs",b"requiredSigs"]) -> None: ...
global___ApprovedBlockCandidateProto = ApprovedBlockCandidateProto

class UnapprovedBlockProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CANDIDATE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def candidate(self) -> global___ApprovedBlockCandidateProto: ...
    timestamp: builtins.int
    duration: builtins.int
    def __init__(self,
        *,
        candidate: typing.Optional[global___ApprovedBlockCandidateProto] = ...,
        timestamp: builtins.int = ...,
        duration: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["candidate",b"candidate"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["candidate",b"candidate","duration",b"duration","timestamp",b"timestamp"]) -> None: ...
global___UnapprovedBlockProto = UnapprovedBlockProto

class Signature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PUBLICKEY_FIELD_NUMBER: builtins.int
    ALGORITHM_FIELD_NUMBER: builtins.int
    SIG_FIELD_NUMBER: builtins.int
    publicKey: builtins.bytes
    algorithm: typing.Text
    sig: builtins.bytes
    def __init__(self,
        *,
        publicKey: builtins.bytes = ...,
        algorithm: typing.Text = ...,
        sig: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["algorithm",b"algorithm","publicKey",b"publicKey","sig",b"sig"]) -> None: ...
global___Signature = Signature

class BlockApprovalProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CANDIDATE_FIELD_NUMBER: builtins.int
    SIG_FIELD_NUMBER: builtins.int
    @property
    def candidate(self) -> global___ApprovedBlockCandidateProto: ...
    @property
    def sig(self) -> global___Signature: ...
    def __init__(self,
        *,
        candidate: typing.Optional[global___ApprovedBlockCandidateProto] = ...,
        sig: typing.Optional[global___Signature] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["candidate",b"candidate","sig",b"sig"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["candidate",b"candidate","sig",b"sig"]) -> None: ...
global___BlockApprovalProto = BlockApprovalProto

class ApprovedBlockProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CANDIDATE_FIELD_NUMBER: builtins.int
    SIGS_FIELD_NUMBER: builtins.int
    @property
    def candidate(self) -> global___ApprovedBlockCandidateProto: ...
    @property
    def sigs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Signature]: ...
    def __init__(self,
        *,
        candidate: typing.Optional[global___ApprovedBlockCandidateProto] = ...,
        sigs: typing.Optional[typing.Iterable[global___Signature]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["candidate",b"candidate"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["candidate",b"candidate","sigs",b"sigs"]) -> None: ...
global___ApprovedBlockProto = ApprovedBlockProto

class ApprovedBlockRequestProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IDENTIFIER_FIELD_NUMBER: builtins.int
    TRIMSTATE_FIELD_NUMBER: builtins.int
    identifier: typing.Text
    trimState: builtins.bool
    def __init__(self,
        *,
        identifier: typing.Text = ...,
        trimState: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["identifier",b"identifier","trimState",b"trimState"]) -> None: ...
global___ApprovedBlockRequestProto = ApprovedBlockRequestProto

class NoApprovedBlockAvailableProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IDENTIFIER_FIELD_NUMBER: builtins.int
    NODEIDENTIFER_FIELD_NUMBER: builtins.int
    identifier: typing.Text
    nodeIdentifer: typing.Text
    def __init__(self,
        *,
        identifier: typing.Text = ...,
        nodeIdentifer: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["identifier",b"identifier","nodeIdentifer",b"nodeIdentifer"]) -> None: ...
global___NoApprovedBlockAvailableProto = NoApprovedBlockAvailableProto

class BlockMessageProto(google.protobuf.message.Message):
    """------- End Signing Protocol --------

    --------- Core Protocol  --------
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BLOCKHASH_FIELD_NUMBER: builtins.int
    HEADER_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    JUSTIFICATIONS_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    SEQNUM_FIELD_NUMBER: builtins.int
    SIG_FIELD_NUMBER: builtins.int
    SIGALGORITHM_FIELD_NUMBER: builtins.int
    SHARDID_FIELD_NUMBER: builtins.int
    EXTRABYTES_FIELD_NUMBER: builtins.int
    blockHash: builtins.bytes
    """obtained by hashing the information in the header"""

    @property
    def header(self) -> global___HeaderProto: ...
    @property
    def body(self) -> global___BodyProto: ...
    @property
    def justifications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JustificationProto]:
        """map of all validators to latest blocks based on current view"""
        pass
    sender: builtins.bytes
    """public key of the validator that created the block"""

    seqNum: builtins.int
    """number of blocks created by the validator"""

    sig: builtins.bytes
    """signature generated by signing `hash(hash(justification) concat blockHash)`."""

    sigAlgorithm: typing.Text
    """name of the algorithm used to sign"""

    shardId: typing.Text
    """identifier of the shard where the block was created"""

    extraBytes: builtins.bytes
    def __init__(self,
        *,
        blockHash: builtins.bytes = ...,
        header: typing.Optional[global___HeaderProto] = ...,
        body: typing.Optional[global___BodyProto] = ...,
        justifications: typing.Optional[typing.Iterable[global___JustificationProto]] = ...,
        sender: builtins.bytes = ...,
        seqNum: builtins.int = ...,
        sig: builtins.bytes = ...,
        sigAlgorithm: typing.Text = ...,
        shardId: typing.Text = ...,
        extraBytes: builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body",b"body","header",b"header"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["blockHash",b"blockHash","body",b"body","extraBytes",b"extraBytes","header",b"header","justifications",b"justifications","sender",b"sender","seqNum",b"seqNum","shardId",b"shardId","sig",b"sig","sigAlgorithm",b"sigAlgorithm"]) -> None: ...
global___BlockMessageProto = BlockMessageProto

class BlockHashMessageProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HASH_FIELD_NUMBER: builtins.int
    BLOCKCREATOR_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    blockCreator: builtins.bytes
    def __init__(self,
        *,
        hash: builtins.bytes = ...,
        blockCreator: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["blockCreator",b"blockCreator","hash",b"hash"]) -> None: ...
global___BlockHashMessageProto = BlockHashMessageProto

class BlockMetadataInternal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BLOCKHASH_FIELD_NUMBER: builtins.int
    PARENTS_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    JUSTIFICATIONS_FIELD_NUMBER: builtins.int
    BONDS_FIELD_NUMBER: builtins.int
    BLOCKNUM_FIELD_NUMBER: builtins.int
    SEQNUM_FIELD_NUMBER: builtins.int
    INVALID_FIELD_NUMBER: builtins.int
    DIRECTLYFINALIZED_FIELD_NUMBER: builtins.int
    FINALIZED_FIELD_NUMBER: builtins.int
    blockHash: builtins.bytes
    @property
    def parents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    sender: builtins.bytes
    @property
    def justifications(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JustificationProto]: ...
    @property
    def bonds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BondProto]: ...
    blockNum: builtins.int
    seqNum: builtins.int
    invalid: builtins.bool
    """whether the block was marked as invalid"""

    directlyFinalized: builtins.bool
    """whether the block has been last finalized block (LFB)"""

    finalized: builtins.bool
    """whether the block is finalized"""

    def __init__(self,
        *,
        blockHash: builtins.bytes = ...,
        parents: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        sender: builtins.bytes = ...,
        justifications: typing.Optional[typing.Iterable[global___JustificationProto]] = ...,
        bonds: typing.Optional[typing.Iterable[global___BondProto]] = ...,
        blockNum: builtins.int = ...,
        seqNum: builtins.int = ...,
        invalid: builtins.bool = ...,
        directlyFinalized: builtins.bool = ...,
        finalized: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["blockHash",b"blockHash","blockNum",b"blockNum","bonds",b"bonds","directlyFinalized",b"directlyFinalized","finalized",b"finalized","invalid",b"invalid","justifications",b"justifications","parents",b"parents","sender",b"sender","seqNum",b"seqNum"]) -> None: ...
global___BlockMetadataInternal = BlockMetadataInternal

class HeaderProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PARENTSHASHLIST_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    EXTRABYTES_FIELD_NUMBER: builtins.int
    @property
    def parentsHashList(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """list of parent block hashes"""
        pass
    timestamp: builtins.int
    version: builtins.int
    extraBytes: builtins.bytes
    def __init__(self,
        *,
        parentsHashList: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        timestamp: builtins.int = ...,
        version: builtins.int = ...,
        extraBytes: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["extraBytes",b"extraBytes","parentsHashList",b"parentsHashList","timestamp",b"timestamp","version",b"version"]) -> None: ...
global___HeaderProto = HeaderProto

class DeployDataProto(google.protobuf.message.Message):
    """*
    Note: deploys are uniquely keyed by `user`, `timestamp`.

    **TODO**: details of signatures and payment. See RHOL-781
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEPLOYER_FIELD_NUMBER: builtins.int
    TERM_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    SIG_FIELD_NUMBER: builtins.int
    SIGALGORITHM_FIELD_NUMBER: builtins.int
    PHLOPRICE_FIELD_NUMBER: builtins.int
    PHLOLIMIT_FIELD_NUMBER: builtins.int
    VALIDAFTERBLOCKNUMBER_FIELD_NUMBER: builtins.int
    SHARDID_FIELD_NUMBER: builtins.int
    deployer: builtins.bytes
    """public key"""

    term: typing.Text
    """rholang source code to deploy (will be parsed into `Par`)"""

    timestamp: builtins.int
    """millisecond timestamp"""

    sig: builtins.bytes
    """signature of (hash(term) + timestamp) using private key"""

    sigAlgorithm: typing.Text
    """name of the algorithm used to sign"""

    phloPrice: builtins.int
    """phlo price"""

    phloLimit: builtins.int
    """phlo limit for the deployment"""

    validAfterBlockNumber: builtins.int
    shardId: typing.Text
    """shard ID to prevent replay of deploys between shards"""

    def __init__(self,
        *,
        deployer: builtins.bytes = ...,
        term: typing.Text = ...,
        timestamp: builtins.int = ...,
        sig: builtins.bytes = ...,
        sigAlgorithm: typing.Text = ...,
        phloPrice: builtins.int = ...,
        phloLimit: builtins.int = ...,
        validAfterBlockNumber: builtins.int = ...,
        shardId: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deployer",b"deployer","phloLimit",b"phloLimit","phloPrice",b"phloPrice","shardId",b"shardId","sig",b"sig","sigAlgorithm",b"sigAlgorithm","term",b"term","timestamp",b"timestamp","validAfterBlockNumber",b"validAfterBlockNumber"]) -> None: ...
global___DeployDataProto = DeployDataProto

class ProcessedDeployProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DEPLOY_FIELD_NUMBER: builtins.int
    COST_FIELD_NUMBER: builtins.int
    DEPLOYLOG_FIELD_NUMBER: builtins.int
    ERRORED_FIELD_NUMBER: builtins.int
    SYSTEMDEPLOYERROR_FIELD_NUMBER: builtins.int
    @property
    def deploy(self) -> global___DeployDataProto: ...
    @property
    def cost(self) -> RhoTypes_pb2.PCost: ...
    @property
    def deployLog(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventProto]:
        """the new terms and comm. rule reductions from this deploy"""
        pass
    errored: builtins.bool
    """true if deploy encountered a user error"""

    systemDeployError: typing.Text
    def __init__(self,
        *,
        deploy: typing.Optional[global___DeployDataProto] = ...,
        cost: typing.Optional[RhoTypes_pb2.PCost] = ...,
        deployLog: typing.Optional[typing.Iterable[global___EventProto]] = ...,
        errored: builtins.bool = ...,
        systemDeployError: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cost",b"cost","deploy",b"deploy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cost",b"cost","deploy",b"deploy","deployLog",b"deployLog","errored",b"errored","systemDeployError",b"systemDeployError"]) -> None: ...
global___ProcessedDeployProto = ProcessedDeployProto

class SlashSystemDeployDataProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INVALIDBLOCKHASH_FIELD_NUMBER: builtins.int
    ISSUERPUBLICKEY_FIELD_NUMBER: builtins.int
    invalidBlockHash: builtins.bytes
    issuerPublicKey: builtins.bytes
    def __init__(self,
        *,
        invalidBlockHash: builtins.bytes = ...,
        issuerPublicKey: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["invalidBlockHash",b"invalidBlockHash","issuerPublicKey",b"issuerPublicKey"]) -> None: ...
global___SlashSystemDeployDataProto = SlashSystemDeployDataProto

class CloseBlockSystemDeployDataProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___CloseBlockSystemDeployDataProto = CloseBlockSystemDeployDataProto

class SystemDeployDataProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SLASHSYSTEMDEPLOY_FIELD_NUMBER: builtins.int
    CLOSEBLOCKSYSTEMDEPLOY_FIELD_NUMBER: builtins.int
    @property
    def slashSystemDeploy(self) -> global___SlashSystemDeployDataProto: ...
    @property
    def closeBlockSystemDeploy(self) -> global___CloseBlockSystemDeployDataProto: ...
    def __init__(self,
        *,
        slashSystemDeploy: typing.Optional[global___SlashSystemDeployDataProto] = ...,
        closeBlockSystemDeploy: typing.Optional[global___CloseBlockSystemDeployDataProto] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["closeBlockSystemDeploy",b"closeBlockSystemDeploy","slashSystemDeploy",b"slashSystemDeploy","systemDeploy",b"systemDeploy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["closeBlockSystemDeploy",b"closeBlockSystemDeploy","slashSystemDeploy",b"slashSystemDeploy","systemDeploy",b"systemDeploy"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["systemDeploy",b"systemDeploy"]) -> typing.Optional[typing_extensions.Literal["slashSystemDeploy","closeBlockSystemDeploy"]]: ...
global___SystemDeployDataProto = SystemDeployDataProto

class ProcessedSystemDeployProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SYSTEMDEPLOY_FIELD_NUMBER: builtins.int
    DEPLOYLOG_FIELD_NUMBER: builtins.int
    ERRORMSG_FIELD_NUMBER: builtins.int
    @property
    def systemDeploy(self) -> global___SystemDeployDataProto: ...
    @property
    def deployLog(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EventProto]: ...
    errorMsg: typing.Text
    def __init__(self,
        *,
        systemDeploy: typing.Optional[global___SystemDeployDataProto] = ...,
        deployLog: typing.Optional[typing.Iterable[global___EventProto]] = ...,
        errorMsg: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["systemDeploy",b"systemDeploy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deployLog",b"deployLog","errorMsg",b"errorMsg","systemDeploy",b"systemDeploy"]) -> None: ...
global___ProcessedSystemDeployProto = ProcessedSystemDeployProto

class BodyProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATE_FIELD_NUMBER: builtins.int
    DEPLOYS_FIELD_NUMBER: builtins.int
    SYSTEMDEPLOYS_FIELD_NUMBER: builtins.int
    EXTRABYTES_FIELD_NUMBER: builtins.int
    REJECTEDDEPLOYS_FIELD_NUMBER: builtins.int
    @property
    def state(self) -> global___RChainStateProto: ...
    @property
    def deploys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProcessedDeployProto]: ...
    @property
    def systemDeploys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProcessedSystemDeployProto]: ...
    extraBytes: builtins.bytes
    @property
    def rejectedDeploys(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RejectedDeployProto]: ...
    def __init__(self,
        *,
        state: typing.Optional[global___RChainStateProto] = ...,
        deploys: typing.Optional[typing.Iterable[global___ProcessedDeployProto]] = ...,
        systemDeploys: typing.Optional[typing.Iterable[global___ProcessedSystemDeployProto]] = ...,
        extraBytes: builtins.bytes = ...,
        rejectedDeploys: typing.Optional[typing.Iterable[global___RejectedDeployProto]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["state",b"state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["deploys",b"deploys","extraBytes",b"extraBytes","rejectedDeploys",b"rejectedDeploys","state",b"state","systemDeploys",b"systemDeploys"]) -> None: ...
global___BodyProto = BodyProto

class RejectedDeployProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SIG_FIELD_NUMBER: builtins.int
    sig: builtins.bytes
    def __init__(self,
        *,
        sig: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sig",b"sig"]) -> None: ...
global___RejectedDeployProto = RejectedDeployProto

class JustificationProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALIDATOR_FIELD_NUMBER: builtins.int
    LATESTBLOCKHASH_FIELD_NUMBER: builtins.int
    validator: builtins.bytes
    latestBlockHash: builtins.bytes
    def __init__(self,
        *,
        validator: builtins.bytes = ...,
        latestBlockHash: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["latestBlockHash",b"latestBlockHash","validator",b"validator"]) -> None: ...
global___JustificationProto = JustificationProto

class RChainStateProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PRESTATEHASH_FIELD_NUMBER: builtins.int
    POSTSTATEHASH_FIELD_NUMBER: builtins.int
    BONDS_FIELD_NUMBER: builtins.int
    BLOCKNUMBER_FIELD_NUMBER: builtins.int
    preStateHash: builtins.bytes
    """hash of the tuplespace contents before new deploys"""

    postStateHash: builtins.bytes
    """hash of the tuplespace contents after new deploys"""

    @property
    def bonds(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BondProto]:
        """Internals of what will be the "blessed" PoS contract
        (which will be part of the tuplespace in the real implementation).
        """
        pass
    blockNumber: builtins.int
    def __init__(self,
        *,
        preStateHash: builtins.bytes = ...,
        postStateHash: builtins.bytes = ...,
        bonds: typing.Optional[typing.Iterable[global___BondProto]] = ...,
        blockNumber: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["blockNumber",b"blockNumber","bonds",b"bonds","postStateHash",b"postStateHash","preStateHash",b"preStateHash"]) -> None: ...
global___RChainStateProto = RChainStateProto

class EventProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PRODUCE_FIELD_NUMBER: builtins.int
    CONSUME_FIELD_NUMBER: builtins.int
    COMM_FIELD_NUMBER: builtins.int
    @property
    def produce(self) -> global___ProduceEventProto: ...
    @property
    def consume(self) -> global___ConsumeEventProto: ...
    @property
    def comm(self) -> global___CommEventProto: ...
    def __init__(self,
        *,
        produce: typing.Optional[global___ProduceEventProto] = ...,
        consume: typing.Optional[global___ConsumeEventProto] = ...,
        comm: typing.Optional[global___CommEventProto] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["comm",b"comm","consume",b"consume","event_instance",b"event_instance","produce",b"produce"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["comm",b"comm","consume",b"consume","event_instance",b"event_instance","produce",b"produce"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["event_instance",b"event_instance"]) -> typing.Optional[typing_extensions.Literal["produce","consume","comm"]]: ...
global___EventProto = EventProto

class ProduceEventProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHANNELSHASH_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    PERSISTENT_FIELD_NUMBER: builtins.int
    TIMESREPEATED_FIELD_NUMBER: builtins.int
    channelsHash: builtins.bytes
    hash: builtins.bytes
    persistent: builtins.bool
    timesRepeated: builtins.int
    def __init__(self,
        *,
        channelsHash: builtins.bytes = ...,
        hash: builtins.bytes = ...,
        persistent: builtins.bool = ...,
        timesRepeated: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["channelsHash",b"channelsHash","hash",b"hash","persistent",b"persistent","timesRepeated",b"timesRepeated"]) -> None: ...
global___ProduceEventProto = ProduceEventProto

class ConsumeEventProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHANNELSHASHES_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    PERSISTENT_FIELD_NUMBER: builtins.int
    @property
    def channelsHashes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    hash: builtins.bytes
    persistent: builtins.bool
    def __init__(self,
        *,
        channelsHashes: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        hash: builtins.bytes = ...,
        persistent: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["channelsHashes",b"channelsHashes","hash",b"hash","persistent",b"persistent"]) -> None: ...
global___ConsumeEventProto = ConsumeEventProto

class CommEventProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONSUME_FIELD_NUMBER: builtins.int
    PRODUCES_FIELD_NUMBER: builtins.int
    PEEKS_FIELD_NUMBER: builtins.int
    @property
    def consume(self) -> global___ConsumeEventProto: ...
    @property
    def produces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ProduceEventProto]: ...
    @property
    def peeks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PeekProto]: ...
    def __init__(self,
        *,
        consume: typing.Optional[global___ConsumeEventProto] = ...,
        produces: typing.Optional[typing.Iterable[global___ProduceEventProto]] = ...,
        peeks: typing.Optional[typing.Iterable[global___PeekProto]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["consume",b"consume"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["consume",b"consume","peeks",b"peeks","produces",b"produces"]) -> None: ...
global___CommEventProto = CommEventProto

class PeekProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHANNELINDEX_FIELD_NUMBER: builtins.int
    channelIndex: builtins.int
    def __init__(self,
        *,
        channelIndex: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["channelIndex",b"channelIndex"]) -> None: ...
global___PeekProto = PeekProto

class BondProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALIDATOR_FIELD_NUMBER: builtins.int
    STAKE_FIELD_NUMBER: builtins.int
    validator: builtins.bytes
    stake: builtins.int
    def __init__(self,
        *,
        validator: builtins.bytes = ...,
        stake: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stake",b"stake","validator",b"validator"]) -> None: ...
global___BondProto = BondProto

class StoreNodeKeyProto(google.protobuf.message.Message):
    """--------- Last finalized state  --------

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HASH_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    index: builtins.int
    def __init__(self,
        *,
        hash: builtins.bytes = ...,
        index: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash",b"hash","index",b"index"]) -> None: ...
global___StoreNodeKeyProto = StoreNodeKeyProto

class StoreItemsMessageRequestProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STARTPATH_FIELD_NUMBER: builtins.int
    SKIP_FIELD_NUMBER: builtins.int
    TAKE_FIELD_NUMBER: builtins.int
    @property
    def startPath(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StoreNodeKeyProto]: ...
    skip: builtins.int
    take: builtins.int
    def __init__(self,
        *,
        startPath: typing.Optional[typing.Iterable[global___StoreNodeKeyProto]] = ...,
        skip: builtins.int = ...,
        take: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["skip",b"skip","startPath",b"startPath","take",b"take"]) -> None: ...
global___StoreItemsMessageRequestProto = StoreItemsMessageRequestProto

class StoreItemProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.bytes
    value: builtins.bytes
    def __init__(self,
        *,
        key: builtins.bytes = ...,
        value: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...
global___StoreItemProto = StoreItemProto

class StoreItemsMessageProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STARTPATH_FIELD_NUMBER: builtins.int
    LASTPATH_FIELD_NUMBER: builtins.int
    HISTORYITEMS_FIELD_NUMBER: builtins.int
    DATAITEMS_FIELD_NUMBER: builtins.int
    @property
    def startPath(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StoreNodeKeyProto]: ...
    @property
    def lastPath(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StoreNodeKeyProto]: ...
    @property
    def historyItems(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StoreItemProto]: ...
    @property
    def dataItems(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StoreItemProto]: ...
    def __init__(self,
        *,
        startPath: typing.Optional[typing.Iterable[global___StoreNodeKeyProto]] = ...,
        lastPath: typing.Optional[typing.Iterable[global___StoreNodeKeyProto]] = ...,
        historyItems: typing.Optional[typing.Iterable[global___StoreItemProto]] = ...,
        dataItems: typing.Optional[typing.Iterable[global___StoreItemProto]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dataItems",b"dataItems","historyItems",b"historyItems","lastPath",b"lastPath","startPath",b"startPath"]) -> None: ...
global___StoreItemsMessageProto = StoreItemsMessageProto
