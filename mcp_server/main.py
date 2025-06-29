# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T12:39:38+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query
from pydantic import conint

from models import (
    AssetsPostRequest,
    ConfigureLogsResponse,
    CreateAssetResponse,
    CreatePackagingConfigurationResponse,
    CreatePackagingGroupResponse,
    DeleteAssetResponse,
    DeletePackagingConfigurationResponse,
    DeletePackagingGroupResponse,
    DescribeAssetResponse,
    DescribePackagingConfigurationResponse,
    DescribePackagingGroupResponse,
    ForbiddenException,
    InternalServerErrorException,
    ListAssetsResponse,
    ListPackagingConfigurationsResponse,
    ListPackagingGroupsResponse,
    ListTagsForResourceResponse,
    NotFoundException,
    PackagingConfigurationsPostRequest,
    PackagingGroupsIdConfigureLogsPutRequest,
    PackagingGroupsIdPutRequest,
    PackagingGroupsPostRequest,
    ServiceUnavailableException,
    TagKeys,
    TagsResourceArnPostRequest,
    TooManyRequestsException,
    UnprocessableEntityException,
    UpdatePackagingGroupResponse,
)

app = MCPProxy(
    contact={
        'email': 'mike.ralphson@gmail.com',
        'name': 'Mike Ralphson',
        'url': 'https://github.com/mermade/aws2openapi',
        'x-twitter': 'PermittedSoc',
    },
    description='AWS Elemental MediaPackage VOD',
    license={'name': 'Apache 2.0 License', 'url': 'http://www.apache.org/licenses/'},
    termsOfService='https://aws.amazon.com/service-terms/',
    title='AWS Elemental MediaPackage VOD',
    version='2018-11-07',
    servers=[
        {
            'description': 'The MediaPackage Vod multi-region endpoint',
            'url': 'http://mediapackage-vod.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The MediaPackage Vod multi-region endpoint',
            'url': 'https://mediapackage-vod.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The MediaPackage Vod endpoint for China (Beijing) and China (Ningxia)',
            'url': 'http://mediapackage-vod.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
        {
            'description': 'The MediaPackage Vod endpoint for China (Beijing) and China (Ningxia)',
            'url': 'https://mediapackage-vod.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
    ],
)


@app.get(
    '/assets',
    description=""" Returns a collection of MediaPackage VOD Asset resources. """,
    tags=['packaging_group_management', 'packaging_configuration_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_assets(
    max_results: Union[
        Optional[conint(ge=1, le=1000)], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='maxResults'),
    next_token: Union[
        Optional[str], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='nextToken'),
    packaging_group_id: Optional[str] = Query(None, alias='packagingGroupId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/assets',
    description=""" Creates a new MediaPackage VOD Asset resource. """,
    tags=[
        'asset_management',
        'packaging_configuration_management',
        'packaging_group_management',
        'resource_tagging',
    ],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_asset(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: AssetsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/assets/{id}',
    description=""" Deletes an existing MediaPackage VOD Asset resource. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_asset(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/assets/{id}',
    description=""" Returns a description of a MediaPackage VOD Asset resource. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_asset(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/packaging_configurations',
    description=""" Returns a collection of MediaPackage VOD PackagingConfiguration resources. """,
    tags=['packaging_group_management', 'packaging_configuration_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_packaging_configurations(
    max_results: Union[
        Optional[conint(ge=1, le=1000)], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='maxResults'),
    next_token: Union[
        Optional[str], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='nextToken'),
    packaging_group_id: Optional[str] = Query(None, alias='packagingGroupId'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/packaging_configurations',
    description=""" Creates a new MediaPackage VOD PackagingConfiguration resource. """,
    tags=['packaging_configuration_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_packaging_configuration(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: PackagingConfigurationsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/packaging_configurations/{id}',
    description=""" Deletes a MediaPackage VOD PackagingConfiguration resource. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_packaging_configuration(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/packaging_configurations/{id}',
    description=""" Returns a description of a MediaPackage VOD PackagingConfiguration resource. """,
    tags=['packaging_configuration_management', 'packaging_group_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_packaging_configuration(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/packaging_groups',
    description=""" Returns a collection of MediaPackage VOD PackagingGroup resources. """,
    tags=['packaging_configuration_management', 'packaging_group_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_packaging_groups(
    max_results: Union[
        Optional[conint(ge=1, le=1000)], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='maxResults'),
    next_token: Union[
        Optional[str], Optional[str], Optional[str], Optional[str]
    ] = Query(None, alias='nextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/packaging_groups',
    description=""" Creates a new MediaPackage VOD PackagingGroup resource. """,
    tags=['packaging_configuration_management', 'packaging_group_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_packaging_group(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: PackagingGroupsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/packaging_groups/{id}',
    description=""" Deletes a MediaPackage VOD PackagingGroup resource. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_packaging_group(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/packaging_groups/{id}',
    description=""" Returns a description of a MediaPackage VOD PackagingGroup resource. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_packaging_group(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/packaging_groups/{id}',
    description=""" Updates a specific packaging group. You can't change the id attribute or any other system-generated attributes. """,
    tags=['packaging_configuration_management', 'packaging_group_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def update_packaging_group(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: PackagingGroupsIdPutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/packaging_groups/{id}/configure_logs',
    description=""" Changes the packaging group's properities to configure log subscription """,
    tags=['packaging_configuration_management', 'packaging_group_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def configure_logs(
    id: str,
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: PackagingGroupsIdConfigureLogsPutRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tags/{resource-arn}',
    description=""" Returns a list of the tags assigned to the specified resource. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_tags_for_resource(
    resource_arn: str = Path(..., alias='resource-arn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/tags/{resource-arn}',
    description=""" Adds tags to the specified resource. You can specify one or more tags to add. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def tag_resource(
    resource_arn: str = Path(..., alias='resource-arn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: TagsResourceArnPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/tags/{resource-arn}#tagKeys',
    description=""" Removes tags from the specified resource. You can specify one or more tags to remove. """,
    tags=['resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def untag_resource(
    resource_arn: str = Path(..., alias='resource-arn'),
    tag_keys: TagKeys = Query(..., alias='tagKeys'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
