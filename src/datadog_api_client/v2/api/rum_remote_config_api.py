# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_sdk_config_response import RumSdkConfigResponse
from datadog_api_client.v2.model.rum_sdk_config_update_request import RumSdkConfigUpdateRequest


class RUMRemoteConfigApi:
    """
    Manage `RUM SDK configurations <https://docs.datadoghq.com/real_user_monitoring/>`_ delivered to RUM applications via Remote Configuration.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_rum_sdk_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumSdkConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/rum/configs/{config_id}",
                "operation_id": "get_rum_sdk_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "config_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_rum_sdk_config_endpoint = _Endpoint(
            settings={
                "response_type": (RumSdkConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/remote_config/products/rum/configs/{config_id}",
                "operation_id": "update_rum_sdk_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "config_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "config_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumSdkConfigUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_rum_sdk_config(
        self,
        config_id: str,
    ) -> RumSdkConfigResponse:
        """Get a RUM SDK configuration.

        Retrieve a RUM SDK configuration by its identifier.

        :param config_id: The ID of the RUM SDK configuration.
        :type config_id: str
        :rtype: RumSdkConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["config_id"] = config_id

        return self._get_rum_sdk_config_endpoint.call_with_http_info(**kwargs)

    def update_rum_sdk_config(
        self,
        config_id: str,
        body: RumSdkConfigUpdateRequest,
    ) -> RumSdkConfigResponse:
        """Update a RUM SDK configuration.

        Update an existing RUM SDK configuration by its identifier.
        Returns the updated configuration when successful.

        :param config_id: The ID of the RUM SDK configuration.
        :type config_id: str
        :param body: The RUM SDK configuration update.
        :type body: RumSdkConfigUpdateRequest
        :rtype: RumSdkConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["config_id"] = config_id

        kwargs["body"] = body

        return self._update_rum_sdk_config_endpoint.call_with_http_info(**kwargs)
