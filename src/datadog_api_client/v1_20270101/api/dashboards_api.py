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
from datadog_api_client.v1_20270101.model.dashboard_summary import DashboardSummary
from datadog_api_client.v1_20270101.model.dashboard_summary_definition import DashboardSummaryDefinition


class DashboardsApi:
    """
    Manage all your dashboards, as well as access to your shared dashboards, through the API. See the `Dashboards page <https://docs.datadoghq.com/dashboards/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_dashboards_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardSummary,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "list_dashboards",
                "http_method": "GET",
                "version": "v1",
            },
            params_map={
                "filter_shared": {
                    "openapi_types": (bool,),
                    "attribute": "filter[shared]",
                    "location": "query",
                },
                "filter_deleted": {
                    "openapi_types": (bool,),
                    "attribute": "filter[deleted]",
                    "location": "query",
                },
                "count": {
                    "openapi_types": (int,),
                    "attribute": "count",
                    "location": "query",
                },
                "start": {
                    "openapi_types": (int,),
                    "attribute": "start",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "api_version": "2027-01-01",
            },
            api_client=api_client,
        )

    def list_dashboards(
        self,
        *,
        filter_shared: Union[bool, UnsetType] = unset,
        filter_deleted: Union[bool, UnsetType] = unset,
        count: Union[int, UnsetType] = unset,
        start: Union[int, UnsetType] = unset,
    ) -> DashboardSummary:
        """Get all dashboards.

        Get all dashboards.

        **Note** : This query will only return custom created or cloned dashboards.
        This query will not return preset dashboards.

        :param filter_shared: When ``true`` , this query only returns shared custom created
            or cloned dashboards.
        :type filter_shared: bool, optional
        :param filter_deleted: When ``true`` , this query returns only deleted custom-created
            or cloned dashboards. This parameter is incompatible with ``filter[shared]``.
        :type filter_deleted: bool, optional
        :param count: The maximum number of dashboards returned in the list.
        :type count: int, optional
        :param start: The specific offset to use as the beginning of the returned response.
        :type start: int, optional
        :rtype: DashboardSummary
        """
        kwargs: Dict[str, Any] = {}
        if filter_shared is not unset:
            kwargs["filter_shared"] = filter_shared

        if filter_deleted is not unset:
            kwargs["filter_deleted"] = filter_deleted

        if count is not unset:
            kwargs["count"] = count

        if start is not unset:
            kwargs["start"] = start

        return self._list_dashboards_endpoint.call_with_http_info(**kwargs)

    def list_dashboards_with_pagination(
        self,
        *,
        filter_shared: Union[bool, UnsetType] = unset,
        filter_deleted: Union[bool, UnsetType] = unset,
        count: Union[int, UnsetType] = unset,
        start: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[DashboardSummaryDefinition]:
        """Get all dashboards.

        Provide a paginated version of :meth:`list_dashboards`, returning all items.

        :param filter_shared: When ``true`` , this query only returns shared custom created
            or cloned dashboards.
        :type filter_shared: bool, optional
        :param filter_deleted: When ``true`` , this query returns only deleted custom-created
            or cloned dashboards. This parameter is incompatible with ``filter[shared]``.
        :type filter_deleted: bool, optional
        :param count: The maximum number of dashboards returned in the list.
        :type count: int, optional
        :param start: The specific offset to use as the beginning of the returned response.
        :type start: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[DashboardSummaryDefinition]
        """
        kwargs: Dict[str, Any] = {}
        if filter_shared is not unset:
            kwargs["filter_shared"] = filter_shared

        if filter_deleted is not unset:
            kwargs["filter_deleted"] = filter_deleted

        if count is not unset:
            kwargs["count"] = count

        if start is not unset:
            kwargs["start"] = start

        local_page_size = get_attribute_from_path(kwargs, "count", 100)
        endpoint = self._list_dashboards_endpoint
        set_attribute_from_path(kwargs, "count", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "dashboards",
            "page_offset_param": "start",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
