# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.vercel_config_response import VercelConfigResponse
from datadog_api_client.v2.model.vercel_config_attributes import VercelConfigAttributes
from datadog_api_client.v2.model.vercel_token_create_request import VercelTokenCreateRequest


class VercelApi:
    """
    Configure the Datadog Vercel integration. Endpoints in this section let you exchange a Vercel marketplace authorization code for a Datadog-managed access token and read or update the logs, traces, and API key configuration associated with a Vercel project.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_vercel_token_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/vercel/token",
                "operation_id": "create_vercel_token",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (VercelTokenCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_vercel_config_endpoint = _Endpoint(
            settings={
                "response_type": (VercelConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/vercel/config/{configuration_id}",
                "operation_id": "get_vercel_config",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "configuration_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "configuration_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_vercel_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/vercel/config/{configuration_id}",
                "operation_id": "update_vercel_config",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "configuration_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "configuration_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (VercelConfigAttributes,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_vercel_token(
        self,
        body: VercelTokenCreateRequest,
    ) -> None:
        """Create Vercel access token.

        Exchange a Vercel marketplace authorization code for an access token and store it in Datadog so that the integration can call Vercel APIs on behalf of the customer. This endpoint is invoked once when a customer installs the Datadog integration from the Vercel marketplace.

        :type body: VercelTokenCreateRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_vercel_token_endpoint.call_with_http_info(**kwargs)

    def get_vercel_config(
        self,
        configuration_id: str,
    ) -> VercelConfigResponse:
        """Get Vercel configuration.

        Retrieve the Datadog Vercel integration configuration for a given Vercel configuration. The response contains the API key reference, logs forwarding settings, and tracing settings stored in Datadog for this configuration.

        :param configuration_id: The Vercel configuration ID.
        :type configuration_id: str
        :rtype: VercelConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["configuration_id"] = configuration_id

        return self._get_vercel_config_endpoint.call_with_http_info(**kwargs)

    def update_vercel_config(
        self,
        configuration_id: str,
        body: VercelConfigAttributes,
    ) -> None:
        """Update Vercel configuration.

        Update the Datadog Vercel integration configuration for a given Vercel configuration. The provided payload replaces the existing API key reference, logs forwarding settings, and tracing settings stored in Datadog for this configuration.

        :param configuration_id: The Vercel configuration ID.
        :type configuration_id: str
        :type body: VercelConfigAttributes
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["configuration_id"] = configuration_id

        kwargs["body"] = body

        return self._update_vercel_config_endpoint.call_with_http_info(**kwargs)
