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
from datadog_api_client.v2.model.single_aggregated_connection_response_array import (
    SingleAggregatedConnectionResponseArray,
)


class CloudNetworkMonitoringApi:
    """
    The Cloud Network Monitoring API allows you to fetch aggregated connections and their attributes. See the `Cloud Network Monitoring page <https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_aggregated_connections_endpoint = _Endpoint(
            settings={
                "response_type": (SingleAggregatedConnectionResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/network/connections/aggregate",
                "operation_id": "get_aggregated_connections",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "_from": {
                    "openapi_types": (int,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "openapi_types": (int,),
                    "attribute": "to",
                    "location": "query",
                },
                "group_by": {
                    "openapi_types": (str,),
                    "attribute": "group_by",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": (str,),
                    "attribute": "tags",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 5000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_aggregated_connections(
        self,
        *,
        _from: Union[int, UnsetType] = unset,
        to: Union[int, UnsetType] = unset,
        group_by: Union[str, UnsetType] = unset,
        tags: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> SingleAggregatedConnectionResponseArray:
        """Get all aggregated connections.

        Get all aggregated connections.

        :param _from: Unix timestamp (number of seconds since epoch) of the start of the query window. If not provided, the start of the query window is 15 minutes before the ``to`` timestamp. If neither ``from`` nor ``to`` are provided, the query window is ``[now - 15m, now]``.
        :type _from: int, optional
        :param to: Unix timestamp (number of seconds since epoch) of the end of the query window. If not provided, the end of the query window is the current time. If neither ``from`` nor ``to`` are provided, the query window is ``[now - 15m, now]``.
        :type to: int, optional
        :param group_by: Comma-separated list of fields to group connections by.
        :type group_by: str, optional
        :param tags: Comma-separated list of tags to filter connections by.
        :type tags: str, optional
        :param limit: The number of connections to be returned. The maximum value is 5000.
        :type limit: int, optional
        :rtype: SingleAggregatedConnectionResponseArray
        """
        kwargs: Dict[str, Any] = {}
        if _from is not unset:
            kwargs["_from"] = _from

        if to is not unset:
            kwargs["to"] = to

        if group_by is not unset:
            kwargs["group_by"] = group_by

        if tags is not unset:
            kwargs["tags"] = tags

        if limit is not unset:
            kwargs["limit"] = limit

        return self._get_aggregated_connections_endpoint.call_with_http_info(**kwargs)
