# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aws_cloud_auth_persona_mappings_response import AWSCloudAuthPersonaMappingsResponse
from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_response import AWSCloudAuthPersonaMappingResponse
from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_create_request import (
    AWSCloudAuthPersonaMappingCreateRequest,
)


class CloudAuthenticationApi:
    """
    Configure AWS cloud authentication mappings for persona and intake authentication through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_aws_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AWSCloudAuthPersonaMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cloud_auth/aws/persona_mapping",
                "operation_id": "create_aws_cloud_auth_persona_mapping",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AWSCloudAuthPersonaMappingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cloud_auth/aws/persona_mapping/{persona_mapping_id}",
                "operation_id": "delete_aws_cloud_auth_persona_mapping",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "persona_mapping_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "persona_mapping_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_aws_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AWSCloudAuthPersonaMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cloud_auth/aws/persona_mapping/{persona_mapping_id}",
                "operation_id": "get_aws_cloud_auth_persona_mapping",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "persona_mapping_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "persona_mapping_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_cloud_auth_persona_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (AWSCloudAuthPersonaMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/cloud_auth/aws/persona_mapping",
                "operation_id": "list_aws_cloud_auth_persona_mappings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_aws_cloud_auth_persona_mapping(
        self,
        body: AWSCloudAuthPersonaMappingCreateRequest,
    ) -> AWSCloudAuthPersonaMappingResponse:
        """Create an AWS cloud authentication persona mapping.

        Create an AWS cloud authentication persona mapping. This endpoint associates an AWS IAM principal with a Datadog user.

        :type body: AWSCloudAuthPersonaMappingCreateRequest
        :rtype: AWSCloudAuthPersonaMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_aws_cloud_auth_persona_mapping_endpoint.call_with_http_info(**kwargs)

    def delete_aws_cloud_auth_persona_mapping(
        self,
        persona_mapping_id: str,
    ) -> None:
        """Delete an AWS cloud authentication persona mapping.

        Delete an AWS cloud authentication persona mapping by ID. This removes the association between an AWS IAM principal and a Datadog user.

        :param persona_mapping_id: The ID of the persona mapping
        :type persona_mapping_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["persona_mapping_id"] = persona_mapping_id

        return self._delete_aws_cloud_auth_persona_mapping_endpoint.call_with_http_info(**kwargs)

    def get_aws_cloud_auth_persona_mapping(
        self,
        persona_mapping_id: str,
    ) -> AWSCloudAuthPersonaMappingResponse:
        """Get an AWS cloud authentication persona mapping.

        Get a specific AWS cloud authentication persona mapping by ID. This endpoint retrieves a single configured persona mapping that associates an AWS IAM principal with a Datadog user.

        :param persona_mapping_id: The ID of the persona mapping
        :type persona_mapping_id: str
        :rtype: AWSCloudAuthPersonaMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["persona_mapping_id"] = persona_mapping_id

        return self._get_aws_cloud_auth_persona_mapping_endpoint.call_with_http_info(**kwargs)

    def list_aws_cloud_auth_persona_mappings(
        self,
    ) -> AWSCloudAuthPersonaMappingsResponse:
        """List AWS cloud authentication persona mappings.

        List all AWS cloud authentication persona mappings. This endpoint retrieves all configured persona mappings that associate AWS IAM principals with Datadog users.

        :rtype: AWSCloudAuthPersonaMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_cloud_auth_persona_mappings_endpoint.call_with_http_info(**kwargs)
