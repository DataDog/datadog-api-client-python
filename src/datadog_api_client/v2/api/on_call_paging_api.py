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
from datadog_api_client.v2.model.create_page_response import CreatePageResponse
from datadog_api_client.v2.model.create_page_request import CreatePageRequest


class OnCallPagingApi:
    """
    Trigger and manage `Datadog On-Call <https://docs.datadoghq.com/service_management/on-call/>`_
    pages directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._acknowledge_on_call_page_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/pages/{page_id}/acknowledge",
                "operation_id": "acknowledge_on_call_page",
                "http_method": "POST",
                "version": "v2",
                "servers": [
                    {
                        "url": "https://{site}",
                        "variables": {
                            "site": {
                                "description": "The globally available endpoint for On-Call.",
                                "default_value": "navy.oncall.datadoghq.com",
                                "enum_values": [
                                    "saffron.oncall.datadoghq.com",
                                    "navy.oncall.datadoghq.com",
                                    "coral.oncall.datadoghq.com",
                                    "teal.oncall.datadoghq.com",
                                    "beige.oncall.datadoghq.eu",
                                ],
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "api.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                ],
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._create_on_call_page_endpoint = _Endpoint(
            settings={
                "response_type": (CreatePageResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/pages",
                "operation_id": "create_on_call_page",
                "http_method": "POST",
                "version": "v2",
                "servers": [
                    {
                        "url": "https://{site}",
                        "variables": {
                            "site": {
                                "description": "The globally available endpoint for On-Call.",
                                "default_value": "navy.oncall.datadoghq.com",
                                "enum_values": [
                                    "saffron.oncall.datadoghq.com",
                                    "navy.oncall.datadoghq.com",
                                    "coral.oncall.datadoghq.com",
                                    "teal.oncall.datadoghq.com",
                                    "beige.oncall.datadoghq.eu",
                                ],
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "api.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                ],
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreatePageRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._escalate_on_call_page_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/pages/{page_id}/escalate",
                "operation_id": "escalate_on_call_page",
                "http_method": "POST",
                "version": "v2",
                "servers": [
                    {
                        "url": "https://{site}",
                        "variables": {
                            "site": {
                                "description": "The globally available endpoint for On-Call.",
                                "default_value": "navy.oncall.datadoghq.com",
                                "enum_values": [
                                    "saffron.oncall.datadoghq.com",
                                    "navy.oncall.datadoghq.com",
                                    "coral.oncall.datadoghq.com",
                                    "teal.oncall.datadoghq.com",
                                    "beige.oncall.datadoghq.eu",
                                ],
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "api.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                ],
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._resolve_on_call_page_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/on-call/pages/{page_id}/resolve",
                "operation_id": "resolve_on_call_page",
                "http_method": "POST",
                "version": "v2",
                "servers": [
                    {
                        "url": "https://{site}",
                        "variables": {
                            "site": {
                                "description": "The globally available endpoint for On-Call.",
                                "default_value": "navy.oncall.datadoghq.com",
                                "enum_values": [
                                    "saffron.oncall.datadoghq.com",
                                    "navy.oncall.datadoghq.com",
                                    "coral.oncall.datadoghq.com",
                                    "teal.oncall.datadoghq.com",
                                    "beige.oncall.datadoghq.eu",
                                ],
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "api.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "api",
                            },
                        },
                    },
                ],
            },
            params_map={
                "page_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "page_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

    def acknowledge_on_call_page(
        self,
        page_id: UUID,
    ) -> None:
        """Acknowledge On-Call Page.

        Acknowledges an On-Call Page.

        :param page_id: The page ID.
        :type page_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        return self._acknowledge_on_call_page_endpoint.call_with_http_info(**kwargs)

    def create_on_call_page(
        self,
        body: CreatePageRequest,
    ) -> CreatePageResponse:
        """Create On-Call Page.

        Trigger a new On-Call Page.

        :type body: CreatePageRequest
        :rtype: CreatePageResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_on_call_page_endpoint.call_with_http_info(**kwargs)

    def escalate_on_call_page(
        self,
        page_id: UUID,
    ) -> None:
        """Escalate On-Call Page.

        Escalates an On-Call Page.

        :param page_id: The page ID.
        :type page_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        return self._escalate_on_call_page_endpoint.call_with_http_info(**kwargs)

    def resolve_on_call_page(
        self,
        page_id: UUID,
    ) -> None:
        """Resolve On-Call Page.

        Resolves an On-Call Page.

        :param page_id: The page ID.
        :type page_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["page_id"] = page_id

        return self._resolve_on_call_page_endpoint.call_with_http_info(**kwargs)
