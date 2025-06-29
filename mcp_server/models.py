# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T12:39:38+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel, conint


class AdMarkers(Enum):
    NONE = 'NONE'
    SCTE35_ENHANCED = 'SCTE35_ENHANCED'
    PASSTHROUGH = 'PASSTHROUGH'


class DeleteAssetRequest(BaseModel):
    pass


class DeleteAssetResponse(BaseModel):
    pass


class DeletePackagingConfigurationRequest(BaseModel):
    pass


class DeletePackagingConfigurationResponse(BaseModel):
    pass


class DeletePackagingGroupRequest(BaseModel):
    pass


class DeletePackagingGroupResponse(BaseModel):
    pass


class DescribeAssetRequest(BaseModel):
    pass


class DescribePackagingConfigurationRequest(BaseModel):
    pass


class DescribePackagingGroupRequest(BaseModel):
    pass


class EncryptionMethod(Enum):
    AES_128 = 'AES_128'
    SAMPLE_AES = 'SAMPLE_AES'


class ForbiddenException(RootModel[Any]):
    root: Any


class InternalServerErrorException(RootModel[Any]):
    root: Any


class ListAssetsRequest(BaseModel):
    pass


class ListPackagingConfigurationsRequest(BaseModel):
    pass


class ListPackagingGroupsRequest(BaseModel):
    pass


class ListTagsForResourceRequest(BaseModel):
    pass


class ManifestLayout(Enum):
    FULL = 'FULL'
    COMPACT = 'COMPACT'


class MaxResults(RootModel[conint(ge=1, le=1000)]):
    root: conint(ge=1, le=1000)


class NotFoundException(RootModel[Any]):
    root: Any


class PresetSpeke20Audio(Enum):
    PRESET_AUDIO_1 = 'PRESET-AUDIO-1'
    PRESET_AUDIO_2 = 'PRESET-AUDIO-2'
    PRESET_AUDIO_3 = 'PRESET-AUDIO-3'
    SHARED = 'SHARED'
    UNENCRYPTED = 'UNENCRYPTED'


class PresetSpeke20Video(Enum):
    PRESET_VIDEO_1 = 'PRESET-VIDEO-1'
    PRESET_VIDEO_2 = 'PRESET-VIDEO-2'
    PRESET_VIDEO_3 = 'PRESET-VIDEO-3'
    PRESET_VIDEO_4 = 'PRESET-VIDEO-4'
    PRESET_VIDEO_5 = 'PRESET-VIDEO-5'
    PRESET_VIDEO_6 = 'PRESET-VIDEO-6'
    PRESET_VIDEO_7 = 'PRESET-VIDEO-7'
    PRESET_VIDEO_8 = 'PRESET-VIDEO-8'
    SHARED = 'SHARED'
    UNENCRYPTED = 'UNENCRYPTED'


class Profile(Enum):
    NONE = 'NONE'
    HBBTV_1_5 = 'HBBTV_1_5'


class ScteMarkersSource(Enum):
    SEGMENTS = 'SEGMENTS'
    MANIFEST = 'MANIFEST'


class SegmentTemplateFormat(Enum):
    NUMBER_WITH_TIMELINE = 'NUMBER_WITH_TIMELINE'
    TIME_WITH_TIMELINE = 'TIME_WITH_TIMELINE'
    NUMBER_WITH_DURATION = 'NUMBER_WITH_DURATION'


class ServiceUnavailableException(RootModel[Any]):
    root: Any


class StreamOrder(Enum):
    ORIGINAL = 'ORIGINAL'
    VIDEO_BITRATE_ASCENDING = 'VIDEO_BITRATE_ASCENDING'
    VIDEO_BITRATE_DESCENDING = 'VIDEO_BITRATE_DESCENDING'


class TooManyRequestsException(RootModel[Any]):
    root: Any


class UnprocessableEntityException(RootModel[Any]):
    root: Any


class UntagResourceRequest(BaseModel):
    pass


class FieldPeriodTriggersElement(Enum):
    ADS = 'ADS'


class FieldBoolean(RootModel[bool]):
    root: bool


class FieldInteger(RootModel[int]):
    root: int


class FieldListOfPeriodTriggersElement(RootModel[List[FieldPeriodTriggersElement]]):
    root: List[FieldPeriodTriggersElement]


class FieldString(RootModel[str]):
    root: str


class AssetsPostRequest(BaseModel):
    id: str = Field(..., description='The unique identifier for the Asset.')
    packagingGroupId: str = Field(
        ..., description='The ID of the PackagingGroup for the Asset.'
    )
    resourceId: Optional[str] = Field(
        None, description='The resource ID to include in SPEKE key requests.'
    )
    sourceArn: str = Field(..., description='ARN of the source object in S3.')
    sourceRoleArn: str = Field(
        ..., description='The IAM role ARN used to access the source S3 bucket.'
    )
    tags: Optional[Dict[str, FieldString]] = Field(
        None, description='A collection of tags associated with a resource'
    )


class Authorization1(BaseModel):
    CdnIdentifierSecret: Optional[FieldString] = None
    SecretsRoleArn: Optional[FieldString] = None


class EgressAccessLogs(BaseModel):
    LogGroupName: Optional[FieldString] = None


class PackagingGroupsPostRequest(BaseModel):
    authorization: Optional[Authorization1] = Field(
        None, description='CDN Authorization credentials'
    )
    egressAccessLogs: Optional[EgressAccessLogs] = Field(
        None, description='Configure egress access logging.'
    )
    id: str = Field(..., description='The ID of the PackagingGroup.')
    tags: Optional[Dict[str, FieldString]] = Field(
        None, description='A collection of tags associated with a resource'
    )


class PackagingGroupsIdPutRequest(BaseModel):
    authorization: Optional[Authorization1] = Field(
        None, description='CDN Authorization credentials'
    )


class PackagingGroupsIdConfigureLogsPutRequest(BaseModel):
    egressAccessLogs: Optional[EgressAccessLogs] = Field(
        None, description='Configure egress access logging.'
    )


class TagsResourceArnPostRequest(BaseModel):
    tags: Dict[str, FieldString] = Field(
        ..., description='A collection of tags associated with a resource'
    )


class TagKeys(RootModel[List[FieldString]]):
    root: List[FieldString]


class Authorization(BaseModel):
    CdnIdentifierSecret: FieldString
    SecretsRoleArn: FieldString


class EgressEndpoint(BaseModel):
    PackagingConfigurationId: Optional[FieldString] = None
    Status: Optional[FieldString] = None
    Url: Optional[FieldString] = None


class EncryptionContractConfiguration(BaseModel):
    PresetSpeke20Audio_1: PresetSpeke20Audio = Field(..., alias='PresetSpeke20Audio')
    PresetSpeke20Video_1: PresetSpeke20Video = Field(..., alias='PresetSpeke20Video')


class StreamSelection(BaseModel):
    MaxVideoBitsPerSecond: Optional[FieldInteger] = None
    MinVideoBitsPerSecond: Optional[FieldInteger] = None
    StreamOrder_1: Optional[StreamOrder] = Field(None, alias='StreamOrder')


class Tags(RootModel[Optional[Dict[str, FieldString]]]):
    root: Optional[Dict[str, FieldString]] = None


class UpdatePackagingGroupRequest(BaseModel):
    Authorization_1: Optional[Authorization] = Field(None, alias='Authorization')


class UpdatePackagingGroupResponse(BaseModel):
    ApproximateAssetCount: Optional[FieldInteger] = None
    Arn: Optional[FieldString] = None
    Authorization_1: Optional[Authorization] = Field(None, alias='Authorization')
    CreatedAt: Optional[FieldString] = None
    DomainName: Optional[FieldString] = None
    EgressAccessLogs_1: Optional[EgressAccessLogs] = Field(
        None, alias='EgressAccessLogs'
    )
    Id: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class FieldListOfEgressEndpoint(RootModel[List[EgressEndpoint]]):
    root: List[EgressEndpoint]


class FieldListOfString(RootModel[List[FieldString]]):
    root: List[FieldString]


class FieldMapOfString(RootModel[Optional[Dict[str, FieldString]]]):
    root: Optional[Dict[str, FieldString]] = None


class AssetShallow(BaseModel):
    Arn: Optional[FieldString] = None
    CreatedAt: Optional[FieldString] = None
    Id: Optional[FieldString] = None
    PackagingGroupId: Optional[FieldString] = None
    ResourceId: Optional[FieldString] = None
    SourceArn: Optional[FieldString] = None
    SourceRoleArn: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class ConfigureLogsRequest(BaseModel):
    EgressAccessLogs_1: Optional[EgressAccessLogs] = Field(
        None, alias='EgressAccessLogs'
    )


class ConfigureLogsResponse(BaseModel):
    Arn: Optional[FieldString] = None
    Authorization_1: Optional[Authorization] = Field(None, alias='Authorization')
    CreatedAt: Optional[FieldString] = None
    DomainName: Optional[FieldString] = None
    EgressAccessLogs_1: Optional[EgressAccessLogs] = Field(
        None, alias='EgressAccessLogs'
    )
    Id: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class CreateAssetRequest(BaseModel):
    Id: FieldString
    PackagingGroupId: FieldString
    ResourceId: Optional[FieldString] = None
    SourceArn: FieldString
    SourceRoleArn: FieldString
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class CreateAssetResponse(BaseModel):
    Arn: Optional[FieldString] = None
    CreatedAt: Optional[FieldString] = None
    EgressEndpoints: Optional[FieldListOfEgressEndpoint] = None
    Id: Optional[FieldString] = None
    PackagingGroupId: Optional[FieldString] = None
    ResourceId: Optional[FieldString] = None
    SourceArn: Optional[FieldString] = None
    SourceRoleArn: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class CreatePackagingGroupRequest(BaseModel):
    Authorization_1: Optional[Authorization] = Field(None, alias='Authorization')
    EgressAccessLogs_1: Optional[EgressAccessLogs] = Field(
        None, alias='EgressAccessLogs'
    )
    Id: FieldString
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class CreatePackagingGroupResponse(BaseModel):
    Arn: Optional[FieldString] = None
    Authorization_1: Optional[Authorization] = Field(None, alias='Authorization')
    CreatedAt: Optional[FieldString] = None
    DomainName: Optional[FieldString] = None
    EgressAccessLogs_1: Optional[EgressAccessLogs] = Field(
        None, alias='EgressAccessLogs'
    )
    Id: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class DashManifest(BaseModel):
    ManifestLayout_1: Optional[ManifestLayout] = Field(None, alias='ManifestLayout')
    ManifestName: Optional[FieldString] = None
    MinBufferTimeSeconds: Optional[FieldInteger] = None
    Profile_1: Optional[Profile] = Field(None, alias='Profile')
    ScteMarkersSource_1: Optional[ScteMarkersSource] = Field(
        None, alias='ScteMarkersSource'
    )
    StreamSelection_1: Optional[StreamSelection] = Field(None, alias='StreamSelection')


class DescribeAssetResponse(BaseModel):
    Arn: Optional[FieldString] = None
    CreatedAt: Optional[FieldString] = None
    EgressEndpoints: Optional[FieldListOfEgressEndpoint] = None
    Id: Optional[FieldString] = None
    PackagingGroupId: Optional[FieldString] = None
    ResourceId: Optional[FieldString] = None
    SourceArn: Optional[FieldString] = None
    SourceRoleArn: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class DescribePackagingGroupResponse(BaseModel):
    ApproximateAssetCount: Optional[FieldInteger] = None
    Arn: Optional[FieldString] = None
    Authorization_1: Optional[Authorization] = Field(None, alias='Authorization')
    CreatedAt: Optional[FieldString] = None
    DomainName: Optional[FieldString] = None
    EgressAccessLogs_1: Optional[EgressAccessLogs] = Field(
        None, alias='EgressAccessLogs'
    )
    Id: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class HlsManifest(BaseModel):
    AdMarkers_1: Optional[AdMarkers] = Field(None, alias='AdMarkers')
    IncludeIframeOnlyStream: Optional[FieldBoolean] = None
    ManifestName: Optional[FieldString] = None
    ProgramDateTimeIntervalSeconds: Optional[FieldInteger] = None
    RepeatExtXKey: Optional[FieldBoolean] = None
    StreamSelection_1: Optional[StreamSelection] = Field(None, alias='StreamSelection')


class ListTagsForResourceResponse(BaseModel):
    Tags: Optional[FieldMapOfString] = None


class MssManifest(BaseModel):
    ManifestName: Optional[FieldString] = None
    StreamSelection_1: Optional[StreamSelection] = Field(None, alias='StreamSelection')


class PackagingGroup(BaseModel):
    ApproximateAssetCount: Optional[FieldInteger] = None
    Arn: Optional[FieldString] = None
    Authorization_1: Optional[Authorization] = Field(None, alias='Authorization')
    CreatedAt: Optional[FieldString] = None
    DomainName: Optional[FieldString] = None
    EgressAccessLogs_1: Optional[EgressAccessLogs] = Field(
        None, alias='EgressAccessLogs'
    )
    Id: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class SpekeKeyProvider(BaseModel):
    EncryptionContractConfiguration_1: Optional[EncryptionContractConfiguration] = (
        Field(None, alias='EncryptionContractConfiguration')
    )
    RoleArn: FieldString
    SystemIds: FieldListOfString
    Url: FieldString


class TagResourceRequest(BaseModel):
    Tags: FieldMapOfString


class FieldListOfAssetShallow(RootModel[List[AssetShallow]]):
    root: List[AssetShallow]


class FieldListOfDashManifest(RootModel[List[DashManifest]]):
    root: List[DashManifest]


class FieldListOfHlsManifest(RootModel[List[HlsManifest]]):
    root: List[HlsManifest]


class FieldListOfMssManifest(RootModel[List[MssManifest]]):
    root: List[MssManifest]


class FieldListOfPackagingGroup(RootModel[List[PackagingGroup]]):
    root: List[PackagingGroup]


class CmafEncryption(BaseModel):
    ConstantInitializationVector: Optional[FieldString] = None
    SpekeKeyProvider_1: SpekeKeyProvider = Field(..., alias='SpekeKeyProvider')


class CmafPackage(BaseModel):
    Encryption: Optional[CmafEncryption] = None
    HlsManifests: FieldListOfHlsManifest
    IncludeEncoderConfigurationInSegments: Optional[FieldBoolean] = None
    SegmentDurationSeconds: Optional[FieldInteger] = None


class DashEncryption(BaseModel):
    SpekeKeyProvider_1: SpekeKeyProvider = Field(..., alias='SpekeKeyProvider')


class DashPackage(BaseModel):
    DashManifests: FieldListOfDashManifest
    Encryption: Optional[DashEncryption] = None
    IncludeEncoderConfigurationInSegments: Optional[FieldBoolean] = None
    IncludeIframeOnlyStream: Optional[FieldBoolean] = None
    PeriodTriggers: Optional[FieldListOfPeriodTriggersElement] = None
    SegmentDurationSeconds: Optional[FieldInteger] = None
    SegmentTemplateFormat_1: Optional[SegmentTemplateFormat] = Field(
        None, alias='SegmentTemplateFormat'
    )


class HlsEncryption(BaseModel):
    ConstantInitializationVector: Optional[FieldString] = None
    EncryptionMethod_1: Optional[EncryptionMethod] = Field(
        None, alias='EncryptionMethod'
    )
    SpekeKeyProvider_1: SpekeKeyProvider = Field(..., alias='SpekeKeyProvider')


class HlsPackage(BaseModel):
    Encryption: Optional[HlsEncryption] = None
    HlsManifests: FieldListOfHlsManifest
    IncludeDvbSubtitles: Optional[FieldBoolean] = None
    SegmentDurationSeconds: Optional[FieldInteger] = None
    UseAudioRenditionGroup: Optional[FieldBoolean] = None


class ListAssetsResponse(BaseModel):
    Assets: Optional[FieldListOfAssetShallow] = None
    NextToken: Optional[FieldString] = None


class ListPackagingGroupsResponse(BaseModel):
    NextToken: Optional[FieldString] = None
    PackagingGroups: Optional[FieldListOfPackagingGroup] = None


class MssEncryption(BaseModel):
    SpekeKeyProvider_1: SpekeKeyProvider = Field(..., alias='SpekeKeyProvider')


class MssPackage(BaseModel):
    Encryption: Optional[MssEncryption] = None
    MssManifests: FieldListOfMssManifest
    SegmentDurationSeconds: Optional[FieldInteger] = None


class PackagingConfiguration(BaseModel):
    Arn: Optional[FieldString] = None
    CmafPackage_1: Optional[CmafPackage] = Field(None, alias='CmafPackage')
    CreatedAt: Optional[FieldString] = None
    DashPackage_1: Optional[DashPackage] = Field(None, alias='DashPackage')
    HlsPackage_1: Optional[HlsPackage] = Field(None, alias='HlsPackage')
    Id: Optional[FieldString] = None
    MssPackage_1: Optional[MssPackage] = Field(None, alias='MssPackage')
    PackagingGroupId: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class FieldListOfPackagingConfiguration(RootModel[List[PackagingConfiguration]]):
    root: List[PackagingConfiguration]


class CmafPackage1(BaseModel):
    Encryption: Optional[CmafEncryption] = None
    HlsManifests: Optional[FieldListOfHlsManifest] = None
    IncludeEncoderConfigurationInSegments: Optional[FieldBoolean] = None
    SegmentDurationSeconds: Optional[FieldInteger] = None


class DashPackage1(BaseModel):
    DashManifests: Optional[FieldListOfDashManifest] = None
    Encryption: Optional[DashEncryption] = None
    IncludeEncoderConfigurationInSegments: Optional[FieldBoolean] = None
    IncludeIframeOnlyStream: Optional[FieldBoolean] = None
    PeriodTriggers: Optional[FieldListOfPeriodTriggersElement] = None
    SegmentDurationSeconds: Optional[FieldInteger] = None
    SegmentTemplateFormat_1: Optional[SegmentTemplateFormat] = Field(
        None, alias='SegmentTemplateFormat'
    )


class HlsPackage1(BaseModel):
    Encryption: Optional[HlsEncryption] = None
    HlsManifests: Optional[FieldListOfHlsManifest] = None
    IncludeDvbSubtitles: Optional[FieldBoolean] = None
    SegmentDurationSeconds: Optional[FieldInteger] = None
    UseAudioRenditionGroup: Optional[FieldBoolean] = None


class MssPackage1(BaseModel):
    Encryption: Optional[MssEncryption] = None
    MssManifests: Optional[FieldListOfMssManifest] = None
    SegmentDurationSeconds: Optional[FieldInteger] = None


class PackagingConfigurationsPostRequest(BaseModel):
    cmafPackage: Optional[CmafPackage1] = Field(
        None, description='A CMAF packaging configuration.'
    )
    dashPackage: Optional[DashPackage1] = Field(
        None,
        description='A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.',
    )
    hlsPackage: Optional[HlsPackage1] = Field(
        None, description='An HTTP Live Streaming (HLS) packaging configuration.'
    )
    id: str = Field(..., description='The ID of the PackagingConfiguration.')
    mssPackage: Optional[MssPackage1] = Field(
        None, description='A Microsoft Smooth Streaming (MSS) PackagingConfiguration.'
    )
    packagingGroupId: str = Field(..., description='The ID of a PackagingGroup.')
    tags: Optional[Dict[str, FieldString]] = Field(
        None, description='A collection of tags associated with a resource'
    )


class CreatePackagingConfigurationRequest(BaseModel):
    CmafPackage_1: Optional[CmafPackage] = Field(None, alias='CmafPackage')
    DashPackage_1: Optional[DashPackage] = Field(None, alias='DashPackage')
    HlsPackage_1: Optional[HlsPackage] = Field(None, alias='HlsPackage')
    Id: FieldString
    MssPackage_1: Optional[MssPackage] = Field(None, alias='MssPackage')
    PackagingGroupId: FieldString
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class CreatePackagingConfigurationResponse(BaseModel):
    Arn: Optional[FieldString] = None
    CmafPackage_1: Optional[CmafPackage] = Field(None, alias='CmafPackage')
    CreatedAt: Optional[FieldString] = None
    DashPackage_1: Optional[DashPackage] = Field(None, alias='DashPackage')
    HlsPackage_1: Optional[HlsPackage] = Field(None, alias='HlsPackage')
    Id: Optional[FieldString] = None
    MssPackage_1: Optional[MssPackage] = Field(None, alias='MssPackage')
    PackagingGroupId: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class DescribePackagingConfigurationResponse(BaseModel):
    Arn: Optional[FieldString] = None
    CmafPackage_1: Optional[CmafPackage] = Field(None, alias='CmafPackage')
    CreatedAt: Optional[FieldString] = None
    DashPackage_1: Optional[DashPackage] = Field(None, alias='DashPackage')
    HlsPackage_1: Optional[HlsPackage] = Field(None, alias='HlsPackage')
    Id: Optional[FieldString] = None
    MssPackage_1: Optional[MssPackage] = Field(None, alias='MssPackage')
    PackagingGroupId: Optional[FieldString] = None
    Tags_1: Optional[Tags] = Field(None, alias='Tags')


class ListPackagingConfigurationsResponse(BaseModel):
    NextToken: Optional[FieldString] = None
    PackagingConfigurations: Optional[FieldListOfPackagingConfiguration] = None
