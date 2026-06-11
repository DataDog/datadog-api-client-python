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
from datadog_api_client.v2.model.network_health_insights_response import NetworkHealthInsightsResponse


class NetworkHealthInsightsApi:
    """
    Analyze network health by surfacing actionable insights for services experiencing connectivity issues.
    Insights are derived from DNS failure data (timeouts, NXDOMAIN, SERVFAIL, general failures),
    TLS certificate health (expired, expiring soon), and security group denials.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_network_health_insights_endpoint = _Endpoint(
            settings={
                "response_type": (NetworkHealthInsightsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/network-health-insights",
                "operation_id": "list_network_health_insights",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "_from": {
                    "openapi_types": (str,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "openapi_types": (str,),
                    "attribute": "to",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def list_network_health_insights(
        self,
        *,
        _from: Union[str, UnsetType] = unset,
        to: Union[str, UnsetType] = unset,
    ) -> NetworkHealthInsightsResponse:
        """List network health insights.

        Return network health insights for the organization within the given time window.
        Insights are produced by analyzing DNS failures pre-classified by ``network-dns-logger`` ,
        TLS certificate metrics, and denied security group connections. Each insight
        identifies the client and server services involved, the type of issue, and the
        magnitude of the failure observed during the query window.

        :param _from: Unix timestamp (number of seconds since epoch) of the start of the query window.
            If not provided, the start of the query window will be 15 minutes before the ``to`` timestamp.
            If neither ``from`` nor ``to`` are provided, the query window will be ``[now - 15m, now]``.
        :type _from: str, optional
        :param to: Unix timestamp (number of seconds since epoch) of the end of the query window.
            If not provided, the end of the query window will be the current time.
            If neither ``from`` nor ``to`` are provided, the query window will be ``[now - 15m, now]``.
        :type to: str, optional
        :rtype: NetworkHealthInsightsResponse
        """
        kwargs: Dict[str, Any] = {}
        if _from is not unset:
            kwargs["_from"] = _from

        if to is not unset:
            kwargs["to"] = to

        return self._list_network_health_insights_endpoint.call_with_http_info(**kwargs)
