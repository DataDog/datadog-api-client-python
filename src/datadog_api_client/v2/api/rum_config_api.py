# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_config_response import RumConfigResponse
from datadog_api_client.v2.model.rum_config_update_request import RumConfigUpdateRequest
from datadog_api_client.v2.model.rum_config_create_request import RumConfigCreateRequest


class RumConfigApi:
    """
    Manage the `Real User Monitoring (RUM) <https://docs.datadoghq.com/real_user_monitoring/>`_ configuration for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config",
                "operation_id": "create_rum_config",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumConfigCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_rum_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config",
                "operation_id": "get_rum_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_rum_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config",
                "operation_id": "update_rum_config",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumConfigUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_rum_config(
        self,
        body: RumConfigCreateRequest,
    ) -> RumConfigResponse:
        """Create the RUM configuration.

        Create the RUM configuration for your organization.
        Returns the RUM configuration object from the request body when the request is successful.

        :param body: The definition of the RUM configuration to create.
        :type body: RumConfigCreateRequest
        :rtype: RumConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_config_endpoint.call_with_http_info(**kwargs)

    def get_rum_config(
        self,
    ) -> RumConfigResponse:
        """Get the RUM configuration.

        Get the RUM configuration for your organization.

        :rtype: RumConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_rum_config_endpoint.call_with_http_info(**kwargs)

    def update_rum_config(
        self,
        body: RumConfigUpdateRequest,
    ) -> RumConfigResponse:
        """Update the RUM configuration.

        Update the RUM configuration for your organization.
        Returns the RUM configuration object from the request body when the request is successful.

        :param body: New definition of the RUM configuration.
        :type body: RumConfigUpdateRequest
        :rtype: RumConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_rum_config_endpoint.call_with_http_info(**kwargs)
