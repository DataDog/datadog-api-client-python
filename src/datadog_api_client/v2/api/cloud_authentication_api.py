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
from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mappings_response import (
    GitHubCloudAuthIntakeMappingsResponse,
)
from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_response import GitHubCloudAuthIntakeMappingResponse
from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_create_request import (
    GitHubCloudAuthIntakeMappingCreateRequest,
)
from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mappings_response import (
    GitHubCloudAuthPersonaMappingsResponse,
)
from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_response import (
    GitHubCloudAuthPersonaMappingResponse,
)
from datadog_api_client.v2.model.git_hub_cloud_auth_persona_mapping_create_request import (
    GitHubCloudAuthPersonaMappingCreateRequest,
)


class CloudAuthenticationApi:
    """
    Configure AWS and GitHub cloud authentication mappings for persona and intake authentication through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_aws_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (AWSCloudAuthPersonaMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._create_git_hub_cloud_auth_intake_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCloudAuthIntakeMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/intake_mapping",
                "operation_id": "create_git_hub_cloud_auth_intake_mapping",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GitHubCloudAuthIntakeMappingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_git_hub_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCloudAuthPersonaMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/persona_mapping",
                "operation_id": "create_git_hub_cloud_auth_persona_mapping",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GitHubCloudAuthPersonaMappingCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_aws_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._delete_git_hub_cloud_auth_intake_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/intake_mapping/{intake_mapping_id}",
                "operation_id": "delete_git_hub_cloud_auth_intake_mapping",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "intake_mapping_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "intake_mapping_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_git_hub_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/persona_mapping/{persona_mapping_id}",
                "operation_id": "delete_git_hub_cloud_auth_persona_mapping",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._get_git_hub_cloud_auth_intake_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCloudAuthIntakeMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/intake_mapping/{intake_mapping_id}",
                "operation_id": "get_git_hub_cloud_auth_intake_mapping",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "intake_mapping_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "intake_mapping_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_git_hub_cloud_auth_persona_mapping_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCloudAuthPersonaMappingResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/persona_mapping/{persona_mapping_id}",
                "operation_id": "get_git_hub_cloud_auth_persona_mapping",
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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

        self._list_git_hub_cloud_auth_intake_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCloudAuthIntakeMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/intake_mapping",
                "operation_id": "list_git_hub_cloud_auth_intake_mappings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_git_hub_cloud_auth_persona_mappings_endpoint = _Endpoint(
            settings={
                "response_type": (GitHubCloudAuthPersonaMappingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/cloud_auth/github/persona_mapping",
                "operation_id": "list_git_hub_cloud_auth_persona_mappings",
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

    def create_git_hub_cloud_auth_intake_mapping(
        self,
        body: GitHubCloudAuthIntakeMappingCreateRequest,
    ) -> GitHubCloudAuthIntakeMappingResponse:
        """Create a GitHub cloud auth intake mapping.

        Create a GitHub cloud authentication intake mapping. This endpoint entitles a matching GitHub Actions OIDC principal to request Datadog API keys.

        :type body: GitHubCloudAuthIntakeMappingCreateRequest
        :rtype: GitHubCloudAuthIntakeMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_git_hub_cloud_auth_intake_mapping_endpoint.call_with_http_info(**kwargs)

    def create_git_hub_cloud_auth_persona_mapping(
        self,
        body: GitHubCloudAuthPersonaMappingCreateRequest,
    ) -> GitHubCloudAuthPersonaMappingResponse:
        """Create a GitHub cloud auth persona mapping.

        Create a GitHub cloud authentication persona mapping. This endpoint associates a GitHub Actions OIDC principal with a Datadog user. The mapped principal can request an impersonation token.

        :type body: GitHubCloudAuthPersonaMappingCreateRequest
        :rtype: GitHubCloudAuthPersonaMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_git_hub_cloud_auth_persona_mapping_endpoint.call_with_http_info(**kwargs)

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

    def delete_git_hub_cloud_auth_intake_mapping(
        self,
        intake_mapping_id: str,
    ) -> None:
        """Delete a GitHub cloud auth intake mapping.

        Delete a GitHub cloud authentication intake mapping by ID. This removes a GitHub Actions OIDC principal's entitlement to request Datadog API keys.

        :param intake_mapping_id: The ID of the intake mapping
        :type intake_mapping_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["intake_mapping_id"] = intake_mapping_id

        return self._delete_git_hub_cloud_auth_intake_mapping_endpoint.call_with_http_info(**kwargs)

    def delete_git_hub_cloud_auth_persona_mapping(
        self,
        persona_mapping_id: str,
    ) -> None:
        """Delete a GitHub cloud auth persona mapping.

        Delete a GitHub cloud authentication persona mapping by ID. This removes the association between a GitHub Actions OIDC principal and a Datadog user.

        :param persona_mapping_id: The ID of the persona mapping
        :type persona_mapping_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["persona_mapping_id"] = persona_mapping_id

        return self._delete_git_hub_cloud_auth_persona_mapping_endpoint.call_with_http_info(**kwargs)

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

    def get_git_hub_cloud_auth_intake_mapping(
        self,
        intake_mapping_id: str,
    ) -> GitHubCloudAuthIntakeMappingResponse:
        """Get a GitHub cloud authentication intake mapping.

        Get a specific GitHub cloud authentication intake mapping by ID. This endpoint retrieves a single configured intake mapping that entitles a matching GitHub Actions OIDC principal to request Datadog API keys.

        :param intake_mapping_id: The ID of the intake mapping
        :type intake_mapping_id: str
        :rtype: GitHubCloudAuthIntakeMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["intake_mapping_id"] = intake_mapping_id

        return self._get_git_hub_cloud_auth_intake_mapping_endpoint.call_with_http_info(**kwargs)

    def get_git_hub_cloud_auth_persona_mapping(
        self,
        persona_mapping_id: str,
    ) -> GitHubCloudAuthPersonaMappingResponse:
        """Get a GitHub cloud authentication persona mapping.

        Get a specific GitHub cloud authentication persona mapping by ID. This endpoint retrieves a single configured persona mapping that associates a GitHub Actions OIDC principal with a Datadog user. The mapped principal can request an impersonation token.

        :param persona_mapping_id: The ID of the persona mapping
        :type persona_mapping_id: str
        :rtype: GitHubCloudAuthPersonaMappingResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["persona_mapping_id"] = persona_mapping_id

        return self._get_git_hub_cloud_auth_persona_mapping_endpoint.call_with_http_info(**kwargs)

    def list_aws_cloud_auth_persona_mappings(
        self,
    ) -> AWSCloudAuthPersonaMappingsResponse:
        """List AWS cloud authentication persona mappings.

        List all AWS cloud authentication persona mappings. This endpoint retrieves all configured persona mappings that associate AWS IAM principals with Datadog users.

        :rtype: AWSCloudAuthPersonaMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_aws_cloud_auth_persona_mappings_endpoint.call_with_http_info(**kwargs)

    def list_git_hub_cloud_auth_intake_mappings(
        self,
    ) -> GitHubCloudAuthIntakeMappingsResponse:
        """List GitHub cloud authentication intake mappings.

        List all GitHub cloud authentication intake mappings. This endpoint retrieves all configured intake mappings that entitle matching GitHub Actions OIDC principals to request Datadog API keys.

        :rtype: GitHubCloudAuthIntakeMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_git_hub_cloud_auth_intake_mappings_endpoint.call_with_http_info(**kwargs)

    def list_git_hub_cloud_auth_persona_mappings(
        self,
    ) -> GitHubCloudAuthPersonaMappingsResponse:
        """List GitHub cloud authentication persona mappings.

        List all GitHub cloud authentication persona mappings. This endpoint retrieves all configured persona mappings that associate GitHub Actions OpenID Connect (OIDC) principals with Datadog users. Mapped principals can request impersonation tokens.

        :rtype: GitHubCloudAuthPersonaMappingsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_git_hub_cloud_auth_persona_mappings_endpoint.call_with_http_info(**kwargs)
