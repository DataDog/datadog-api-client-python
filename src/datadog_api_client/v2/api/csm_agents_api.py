# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.csm_agents_response import CsmAgentsResponse
from datadog_api_client.v2.model.order_direction import OrderDirection


class CSMAgentsApi:
    """
    Datadog Cloud Security Management (CSM) delivers real-time threat detection
    and continuous configuration audits across your entire cloud infrastructure,
    all in a unified view for seamless collaboration and faster remediation.
    Go to https://docs.datadoghq.com/security/cloud_security_management to learn more
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_all_csm_agents_endpoint = _Endpoint(
            settings={
                "response_type": (CsmAgentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/onboarding/agents",
                "operation_id": "list_all_csm_agents",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page": {
                    "validation": {
                        "inclusive_maximum": 1000000,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "size",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "order_direction": {
                    "openapi_types": (OrderDirection,),
                    "attribute": "order_direction",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_all_csm_serverless_agents_endpoint = _Endpoint(
            settings={
                "response_type": (CsmAgentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/csm/onboarding/serverless/agents",
                "operation_id": "list_all_csm_serverless_agents",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page": {
                    "validation": {
                        "inclusive_maximum": 1000000,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
                "size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "size",
                    "location": "query",
                },
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "order_direction": {
                    "openapi_types": (OrderDirection,),
                    "attribute": "order_direction",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_all_csm_agents(
        self,
        *,
        page: Union[int, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        order_direction: Union[OrderDirection, UnsetType] = unset,
    ) -> CsmAgentsResponse:
        """Get all CSM Agents.

        Get the list of all CSM Agents running on your hosts and containers.

        :param page: The page index for pagination (zero-based).
        :type page: int, optional
        :param size: The number of items to include in a single page.
        :type size: int, optional
        :param query: A search query string to filter results (for example, ``hostname:COMP-T2H4J27423`` ).
        :type query: str, optional
        :param order_direction: The sort direction for results. Use ``asc`` for ascending or ``desc`` for descending.
        :type order_direction: OrderDirection, optional
        :rtype: CsmAgentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page is not unset:
            kwargs["page"] = page

        if size is not unset:
            kwargs["size"] = size

        if query is not unset:
            kwargs["query"] = query

        if order_direction is not unset:
            kwargs["order_direction"] = order_direction

        return self._list_all_csm_agents_endpoint.call_with_http_info(**kwargs)

    def list_all_csm_serverless_agents(
        self,
        *,
        page: Union[int, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        order_direction: Union[OrderDirection, UnsetType] = unset,
    ) -> CsmAgentsResponse:
        """Get all CSM Serverless Agents.

        Get the list of all CSM Serverless Agents running on your hosts and containers.

        :param page: The page index for pagination (zero-based).
        :type page: int, optional
        :param size: The number of items to include in a single page.
        :type size: int, optional
        :param query: A search query string to filter results (for example, ``hostname:COMP-T2H4J27423`` ).
        :type query: str, optional
        :param order_direction: The sort direction for results. Use ``asc`` for ascending or ``desc`` for descending.
        :type order_direction: OrderDirection, optional
        :rtype: CsmAgentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page is not unset:
            kwargs["page"] = page

        if size is not unset:
            kwargs["size"] = size

        if query is not unset:
            kwargs["query"] = query

        if order_direction is not unset:
            kwargs["order_direction"] = order_direction

        return self._list_all_csm_serverless_agents_endpoint.call_with_http_info(**kwargs)
