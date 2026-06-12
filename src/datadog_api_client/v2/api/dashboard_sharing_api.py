# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.list_shared_dashboards_response import ListSharedDashboardsResponse


class DashboardSharingApi:
    """
    Manage dashboard sharing configurations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._list_shared_dashboards_by_dashboard_id_endpoint = _Endpoint(
            settings={
                "response_type": (ListSharedDashboardsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboard/{dashboard_id}/shared",
                "operation_id": "list_shared_dashboards_by_dashboard_id",
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

    def list_shared_dashboards_by_dashboard_id(
        self,
        dashboard_id: str,
    ) -> ListSharedDashboardsResponse:
        """List shared dashboards for a dashboard.

        Retrieve shared dashboards associated with the specified dashboard.

        :param dashboard_id: ID of the dashboard.
        :type dashboard_id: str
        :rtype: ListSharedDashboardsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        return self._list_shared_dashboards_by_dashboard_id_endpoint.call_with_http_info(**kwargs)
