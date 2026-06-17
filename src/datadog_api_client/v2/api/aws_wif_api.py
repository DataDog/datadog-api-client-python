# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UUID,
)
from datadog_api_client.v2.model.aws_wif_intake_mappings_response import AwsWifIntakeMappingsResponse
from datadog_api_client.v2.model.aws_wif_intake_mapping_response import AwsWifIntakeMappingResponse
from datadog_api_client.v2.model.aws_wif_intake_mapping_create_request import AwsWifIntakeMappingCreateRequest
from datadog_api_client.v2.model.aws_wif_persona_mappings_response import AwsWifPersonaMappingsResponse
from datadog_api_client.v2.model.aws_wif_persona_mapping_response import AwsWifPersonaMappingResponse
from datadog_api_client.v2.model.aws_wif_persona_mapping_create_request import AwsWifPersonaMappingCreateRequest


class AWSWIFApi:
    """
    Manage AWS Workload Identity Federation (WIF) mappings.
    Persona mappings link IAM role ARN patterns to Datadog users for delegated-token authentication.
    Intake mappings link IAM role ARN patterns to managed-rotation API keys for agent telemetry ingestion.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_aws_wif_intake_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AwsWifIntakeMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/intake_mapping",
                "operation_id": "create_aws_wif_intake_mapping",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AwsWifIntakeMappingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_aws_wif_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AwsWifPersonaMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/persona_mapping",
                "operation_id": "create_aws_wif_persona_mapping",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AwsWifPersonaMappingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_wif_intake_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/intake_mapping/{config_uuid}",
                "operation_id": "delete_aws_wif_intake_mapping",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "config_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "config_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_aws_wif_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/persona_mapping/{config_uuid}",
                "operation_id": "delete_aws_wif_persona_mapping",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "config_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "config_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_aws_wif_intake_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AwsWifIntakeMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/intake_mapping/{config_uuid}",
                "operation_id": "get_aws_wif_intake_mapping",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "config_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "config_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_aws_wif_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AwsWifPersonaMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/persona_mapping/{config_uuid}",
                "operation_id": "get_aws_wif_persona_mapping",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "config_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "config_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_wif_intake_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (AwsWifIntakeMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/intake_mapping",
                "operation_id": "list_aws_wif_intake_mappings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_aws_wif_persona_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (AwsWifPersonaMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/wif/aws/persona_mapping",
                "operation_id": "list_aws_wif_persona_mappings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_aws_wif_intake_mapping(
        self,
        body: AwsWifIntakeMappingCreateRequest,
    ) -> AwsWifIntakeMappingResponse:
        """Create an AWS WIF intake mapping.

        Create an AWS WIF intake mapping. The mapping binds an IAM role ARN pattern to a managed-rotation API key, allowing AWS workloads to send telemetry to Datadog without requiring a delegated user token.

        :type body: AwsWifIntakeMappingCreateRequest
        :rtype: AwsWifIntakeMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_aws_wif_intake_mapping_endpoint.call_with_http_info(**kwargs)

    def create_aws_wif_persona_mapping(
        self,
        body: AwsWifPersonaMappingCreateRequest,
    ) -> AwsWifPersonaMappingResponse:
        """Create an AWS WIF persona mapping.

        Create an AWS Workload Identity Federation (WIF) persona mapping. The mapping binds an IAM role ARN pattern to a Datadog user handle, which is used to authenticate delegated-token requests from that AWS identity.

        :type body: AwsWifPersonaMappingCreateRequest
        :rtype: AwsWifPersonaMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_aws_wif_persona_mapping_endpoint.call_with_http_info(**kwargs)

    def delete_aws_wif_intake_mapping(
        self,
        config_uuid: UUID,
    ) -> None:
        """Delete an AWS WIF intake mapping.

        Delete an AWS WIF intake mapping by UUID. The associated managed-rotation API key is left intact, but AWS workloads that previously matched this mapping will lose intake access.

        :param config_uuid: The UUID of the WIF configuration to operate on.
        :type config_uuid: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["config_uuid"] = config_uuid

        return self._delete_aws_wif_intake_mapping_endpoint.call_with_http_info(**kwargs)

    def delete_aws_wif_persona_mapping(
        self,
        config_uuid: UUID,
    ) -> None:
        """Delete an AWS WIF persona mapping.

        Delete an AWS WIF persona mapping by UUID. Subsequent delegated-token requests from the previously mapped AWS identity will be denied.

        :param config_uuid: The UUID of the WIF configuration to operate on.
        :type config_uuid: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["config_uuid"] = config_uuid

        return self._delete_aws_wif_persona_mapping_endpoint.call_with_http_info(**kwargs)

    def get_aws_wif_intake_mapping(
        self,
        config_uuid: UUID,
    ) -> AwsWifIntakeMappingResponse:
        """Get an AWS WIF intake mapping.

        Retrieve a single AWS WIF intake mapping by UUID.

        :param config_uuid: The UUID of the WIF configuration to operate on.
        :type config_uuid: UUID
        :rtype: AwsWifIntakeMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["config_uuid"] = config_uuid

        return self._get_aws_wif_intake_mapping_endpoint.call_with_http_info(**kwargs)

    def get_aws_wif_persona_mapping(
        self,
        config_uuid: UUID,
    ) -> AwsWifPersonaMappingResponse:
        """Get an AWS WIF persona mapping.

        Retrieve a single AWS WIF persona mapping by UUID.

        :param config_uuid: The UUID of the WIF configuration to operate on.
        :type config_uuid: UUID
        :rtype: AwsWifPersonaMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["config_uuid"] = config_uuid

        return self._get_aws_wif_persona_mapping_endpoint.call_with_http_info(**kwargs)

    def list_aws_wif_intake_mappings(
        self,
    ) -> AwsWifIntakeMappingsResponse:
        """List AWS WIF intake mappings.

        List every AWS WIF intake mapping configured for the caller's organization.

        :rtype: AwsWifIntakeMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_wif_intake_mappings_endpoint.call_with_http_info(**kwargs)

    def list_aws_wif_persona_mappings(
        self,
    ) -> AwsWifPersonaMappingsResponse:
        """List AWS WIF persona mappings.

        List every AWS WIF persona mapping configured for the caller's organization.

        :rtype: AwsWifPersonaMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_wif_persona_mappings_endpoint.call_with_http_info(**kwargs)
