# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v1_20270101.model.dashboard import Dashboard


class DashboardsApi:
    """
    Manage all your dashboards, as well as access to your shared dashboards, through the API. See the `Dashboards page <https://docs.datadoghq.com/dashboards/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (Dashboard,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "create_dashboard",
                "http_method": "POST",
                "version": "v1",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Dashboard,),
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "api_version": "2027-01-01",
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (Dashboard,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/{dashboard_id}",
                "operation_id": "get_dashboard",
                "http_method": "GET",
                "version": "v1",
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
                "api_version": "2027-01-01",
            },
            api_client=api_client,
        )

        self._update_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (Dashboard,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/{dashboard_id}",
                "operation_id": "update_dashboard",
                "http_method": "PUT",
                "version": "v1",
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Dashboard,),
                    "location": "body",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "api_version": "2027-01-01",
                "content_type": ["application/json"],
            },
            api_client=api_client,
        )

    def create_dashboard(
        self,
        body: Dashboard,
    ) -> Dashboard:
        """Create a new dashboard.

        Create a dashboard using the specified options. When defining queries in your widgets, take note of which queries should have the ``as_count()`` or ``as_rate()`` modifiers appended.
        Refer to the following `documentation <https://docs.datadoghq.com/developers/metrics/type_modifiers/?tab=count#in-application-modifiers>`_ for more information on these modifiers.

        :param body: Create a dashboard request body.
        :type body: Dashboard
        :rtype: Dashboard
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_dashboard_endpoint.call_with_http_info(**kwargs)

    def get_dashboard(
        self,
        dashboard_id: str,
    ) -> Dashboard:
        """Get a dashboard.

        Get a dashboard using the specified ID.

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :rtype: Dashboard
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        return self._get_dashboard_endpoint.call_with_http_info(**kwargs)

    def update_dashboard(
        self,
        dashboard_id: str,
        body: Dashboard,
    ) -> Dashboard:
        """Update a dashboard.

        Update a dashboard using the specified ID.

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :param body: Update Dashboard request body.
        :type body: Dashboard
        :rtype: Dashboard
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["body"] = body

        return self._update_dashboard_endpoint.call_with_http_info(**kwargs)
