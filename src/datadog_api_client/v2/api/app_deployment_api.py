# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.disable_app_response import DisableAppResponse
from datadog_api_client.v2.model.deploy_app_response import DeployAppResponse


class AppDeploymentApi:
    """
    Deploy and disable apps in App Builder.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._deploy_app_endpoint = _Endpoint(
            settings={
                "response_type": (DeployAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps/{app_id}/deployment",
                "operation_id": "deploy_app",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._disable_app_endpoint = _Endpoint(
            settings={
                "response_type": (DisableAppResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/app-builder/apps/{app_id}/deployment",
                "operation_id": "disable_app",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "app_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def deploy_app(
        self,
        app_id: str,
    ) -> DeployAppResponse:
        """Deploy App.

        Deploy (publish) an app by ID

        :type app_id: str
        :rtype: DeployAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._deploy_app_endpoint.call_with_http_info(**kwargs)

    def disable_app(
        self,
        app_id: str,
    ) -> DisableAppResponse:
        """Disable App.

        Disable an app by ID

        :type app_id: str
        :rtype: DisableAppResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["app_id"] = app_id

        return self._disable_app_endpoint.call_with_http_info(**kwargs)
