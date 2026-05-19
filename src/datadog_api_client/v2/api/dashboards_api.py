# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_dashboards_usage_response import ListDashboardsUsageResponse
from datadog_api_client.v2.model.dashboard_usage import DashboardUsage
from datadog_api_client.v2.model.dashboard_usage_response import DashboardUsageResponse


class DashboardsApi:
    """
    Get usage statistics for the dashboards in your organization, including view
    counts, last-edit times, widget counts, and quality scores. See the
    `Dashboards documentation <https://docs.datadoghq.com/dashboards/>`_ for more
    information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._get_dashboard_usage_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardUsageResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboards/{dashboard_id}/usage",
                "operation_id": "get_dashboard_usage",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_dashboards_usage_endpoint = _Endpoint(
            settings={
                "response_type": (ListDashboardsUsageResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboards/usage",
                "operation_id": "list_dashboards_usage",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def get_dashboard_usage(
        self,
        dashboard_id: str,
    ) -> DashboardUsageResponse:
        """Get usage stats for a dashboard.

        Get usage statistics for a single dashboard. The response includes view counts, the most recent view and edit times, widget counts, and the dashboard quality score.

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :rtype: DashboardUsageResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        return self._get_dashboard_usage_endpoint.call_with_http_info(**kwargs)

    def list_dashboards_usage(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> ListDashboardsUsageResponse:
        """Get usage stats for all dashboards.

        Get paginated usage statistics for every dashboard in the caller's organization. Use ``page[limit]`` and ``page[offset]`` to walk the result set.

        :param page_limit: Maximum number of dashboards to return per page. Server-side maximum is 500; values above 500 return a 400 Bad Request.
        :type page_limit: int, optional
        :param page_offset: Zero-based offset into the result set.
        :type page_offset: int, optional
        :rtype: ListDashboardsUsageResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_dashboards_usage_endpoint.call_with_http_info(**kwargs)

    def list_dashboards_usage_with_pagination(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[DashboardUsage]:
        """Get usage stats for all dashboards.

        Provide a paginated version of :meth:`list_dashboards_usage`, returning all items.

        :param page_limit: Maximum number of dashboards to return per page. Server-side maximum is 500; values above 500 return a 400 Bad Request.
        :type page_limit: int, optional
        :param page_offset: Zero-based offset into the result set.
        :type page_offset: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[DashboardUsage]
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 250)
        endpoint = self._list_dashboards_usage_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
