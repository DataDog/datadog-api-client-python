# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v1.model.dashboard_bulk_delete_request import DashboardBulkDeleteRequest
from datadog_api_client.v1.model.dashboard_summary import DashboardSummary
from datadog_api_client.v1.model.dashboard_restore_request import DashboardRestoreRequest
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_delete_response import DashboardDeleteResponse


class DashboardsApi:
    """
    Interact with your dashboard lists through the API to make it easier to organize,
    find, and share all of your dashboards with your team and organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (Dashboard,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "create_dashboard",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Dashboard,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/{dashboard_id}",
                "operation_id": "delete_dashboard",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
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
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_dashboards_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "delete_dashboards",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DashboardBulkDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
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
                "servers": None,
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
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_dashboards_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardSummary,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "list_dashboards",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
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
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._restore_dashboards_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "restore_dashboards",
                "http_method": "PATCH",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DashboardRestoreRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
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
                "servers": None,
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
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
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

    def delete_dashboard(
        self,
        dashboard_id: str,
    ) -> DashboardDeleteResponse:
        """Delete a dashboard.

        Delete a dashboard using the specified ID.

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :rtype: DashboardDeleteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        return self._delete_dashboard_endpoint.call_with_http_info(**kwargs)

    def delete_dashboards(
        self,
        body: DashboardBulkDeleteRequest,
    ) -> None:
        """Delete dashboards.

        Delete dashboards using the specified IDs. If there are any failures, no dashboards will be deleted (partial success is not allowed).

        :param body: Delete dashboards request body.
        :type body: DashboardBulkDeleteRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_dashboards_endpoint.call_with_http_info(**kwargs)

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

    def list_dashboards(
        self,
        *,
        filter_shared: Union[bool, UnsetType] = unset,
        filter_deleted: Union[bool, UnsetType] = unset,
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
        :rtype: DashboardSummary
        """
        kwargs: Dict[str, Any] = {}
        if filter_shared is not unset:
            kwargs["filter_shared"] = filter_shared

        if filter_deleted is not unset:
            kwargs["filter_deleted"] = filter_deleted

        return self._list_dashboards_endpoint.call_with_http_info(**kwargs)

    def restore_dashboards(
        self,
        body: DashboardRestoreRequest,
    ) -> None:
        """Restore deleted dashboards.

        Restore dashboards using the specified IDs. If there are any failures, no dashboards will be restored (partial success is not allowed).

        :param body: Restore dashboards request body.
        :type body: DashboardRestoreRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._restore_dashboards_endpoint.call_with_http_info(**kwargs)

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
