# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_rate_limit_scope_type import RumRateLimitScopeType
from datadog_api_client.v2.model.rum_rate_limit_config_response import RumRateLimitConfigResponse
from datadog_api_client.v2.model.rum_rate_limit_config_update_request import RumRateLimitConfigUpdateRequest


class RumRateLimitApi:
    """
    Manage RUM rate limit configurations for your organization's RUM applications.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._delete_rum_rate_limit_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/rate-limit/{scope_type}/{scope_id}",
                "operation_id": "delete_rum_rate_limit_config",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "scope_type": {
                    "required": True,
                    "openapi_types": (RumRateLimitScopeType,),
                    "attribute": "scope_type",
                    "location": "path",
                },
                "scope_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "scope_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_rum_rate_limit_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumRateLimitConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/rate-limit/{scope_type}/{scope_id}",
                "operation_id": "get_rum_rate_limit_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "scope_type": {
                    "required": True,
                    "openapi_types": (RumRateLimitScopeType,),
                    "attribute": "scope_type",
                    "location": "path",
                },
                "scope_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "scope_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_rum_rate_limit_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumRateLimitConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/rate-limit/{scope_type}/{scope_id}",
                "operation_id": "update_rum_rate_limit_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "scope_type": {
                    "required": True,
                    "openapi_types": (RumRateLimitScopeType,),
                    "attribute": "scope_type",
                    "location": "path",
                },
                "scope_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "scope_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumRateLimitConfigUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def delete_rum_rate_limit_config(
        self,
        scope_type: RumRateLimitScopeType,
        scope_id: str,
    ) -> None:
        """Delete a RUM rate limit configuration.

        Delete the RUM rate limit configuration for a given scope.

        :param scope_type: The type of scope the rate limit configuration applies to.
        :type scope_type: RumRateLimitScopeType
        :param scope_id: The identifier of the scope the rate limit configuration applies to.
            For the ``application`` scope, this is the RUM application ID.
        :type scope_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["scope_type"] = scope_type

        kwargs["scope_id"] = scope_id

        return self._delete_rum_rate_limit_config_endpoint.call_with_http_info(**kwargs)

    def get_rum_rate_limit_config(
        self,
        scope_type: RumRateLimitScopeType,
        scope_id: str,
    ) -> RumRateLimitConfigResponse:
        """Get a RUM rate limit configuration.

        Get the RUM rate limit configuration for a given scope.

        :param scope_type: The type of scope the rate limit configuration applies to.
        :type scope_type: RumRateLimitScopeType
        :param scope_id: The identifier of the scope the rate limit configuration applies to.
            For the ``application`` scope, this is the RUM application ID.
        :type scope_id: str
        :rtype: RumRateLimitConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["scope_type"] = scope_type

        kwargs["scope_id"] = scope_id

        return self._get_rum_rate_limit_config_endpoint.call_with_http_info(**kwargs)

    def update_rum_rate_limit_config(
        self,
        scope_type: RumRateLimitScopeType,
        scope_id: str,
        body: RumRateLimitConfigUpdateRequest,
    ) -> RumRateLimitConfigResponse:
        """Create or update a RUM rate limit configuration.

        Create or update the RUM rate limit configuration for a given scope.
        Returns the rate limit configuration object when the request is successful.

        :param scope_type: The type of scope the rate limit configuration applies to.
        :type scope_type: RumRateLimitScopeType
        :param scope_id: The identifier of the scope the rate limit configuration applies to.
            For the ``application`` scope, this is the RUM application ID.
        :type scope_id: str
        :param body: The definition of the RUM rate limit configuration to create or update.
        :type body: RumRateLimitConfigUpdateRequest
        :rtype: RumRateLimitConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["scope_type"] = scope_type

        kwargs["scope_id"] = scope_id

        kwargs["body"] = body

        return self._update_rum_rate_limit_config_endpoint.call_with_http_info(**kwargs)
