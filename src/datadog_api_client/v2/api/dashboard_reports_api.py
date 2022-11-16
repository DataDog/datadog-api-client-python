# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.dashboard_reports_response import DashboardReportsResponse
from datadog_api_client.v2.model.dashboard_report_response import DashboardReportResponse
from datadog_api_client.v2.model.dashboard_report_create_request import DashboardReportCreateRequest
from datadog_api_client.v2.model.dashboard_report_update_request import DashboardReportUpdateRequest


class DashboardReportsApi:
    """
    Dashboard reports allow for sending scheduled emails with snapshots of your dashboard's widgets, using a given timeframe and frequency, to multiple email recipients.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_dashboard_report_config_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardReportResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboards/{dashboard_id}/reports",
                "operation_id": "create_dashboard_report_config",
                "http_method": "POST",
                "version": "v2",
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
                    "openapi_types": (DashboardReportCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_dashboard_report_config_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboards/{dashboard_id}/reports/{report_uuid}",
                "operation_id": "delete_dashboard_report_config",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "report_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "report_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_dashboard_report_config_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardReportResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboards/{dashboard_id}/reports/{report_uuid}",
                "operation_id": "get_dashboard_report_config",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "report_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "report_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_dashboard_report_configs_list_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardReportsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboards/{dashboard_id}/reports",
                "operation_id": "get_dashboard_report_configs_list",
                "http_method": "GET",
                "version": "v2",
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

        self._update_dashboard_report_config_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardReportResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/dashboards/{dashboard_id}/reports/{report_uuid}",
                "operation_id": "update_dashboard_report_config",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "report_uuid": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "report_uuid",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DashboardReportUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_dashboard_report_config(
        self,
        dashboard_id: str,
        body: DashboardReportCreateRequest,
    ) -> DashboardReportResponse:
        """Create a new Dashboard Report.

        New dashboard report configuration for a given dashboard. This creates a new report email schedule, frequency, timeframe, and more.

        :param dashboard_id: ID of the dashboard for which to create a dashboard report.
        :type dashboard_id: str
        :type body: DashboardReportCreateRequest
        :rtype: DashboardReportResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["body"] = body

        return self._create_dashboard_report_config_endpoint.call_with_http_info(**kwargs)

    def delete_dashboard_report_config(
        self,
        dashboard_id: str,
        report_uuid: str,
    ) -> None:
        """Delete a Dashboard Report.

        Delete a dashboard report configuration, disabling the sending of scheduled emails for this report in the future. This operation cannot be undone. To pause the sending of emails for this report without deleting it, deactivate the report with a ``PATCH`` request.

        :param dashboard_id: ID of the dashboard for which to delete the associated report.
        :type dashboard_id: str
        :param report_uuid: ID of the dashboard report to delete.
        :type report_uuid: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["report_uuid"] = report_uuid

        return self._delete_dashboard_report_config_endpoint.call_with_http_info(**kwargs)

    def get_dashboard_report_config(
        self,
        dashboard_id: str,
        report_uuid: str,
    ) -> DashboardReportResponse:
        """Get a Dashboard Report.

        Fetch a single Dashboard Report configuration. This includes the same information provided when fetching a dashboard's list of currently configured reports, but only for singular reports.

        :param dashboard_id: ID of the dashboard for which to get the associated dashboard report.
        :type dashboard_id: str
        :param report_uuid: ID of the dashboard report to get.
        :type report_uuid: str
        :rtype: DashboardReportResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["report_uuid"] = report_uuid

        return self._get_dashboard_report_config_endpoint.call_with_http_info(**kwargs)

    def get_dashboard_report_configs_list(
        self,
        dashboard_id: str,
    ) -> DashboardReportsResponse:
        """Get Dashboard Reports for a Dashboard.

        List of the dashboard reports configured on a given dashboard. This list includes report configurations that are both enabled and disabled, but does not include reports that have been deleted for the given dashboard.

        :param dashboard_id: ID of the Dashboard for which to get all dashboard reports.
        :type dashboard_id: str
        :rtype: DashboardReportsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        return self._get_dashboard_report_configs_list_endpoint.call_with_http_info(**kwargs)

    def update_dashboard_report_config(
        self,
        dashboard_id: str,
        report_uuid: str,
        body: DashboardReportUpdateRequest,
    ) -> DashboardReportResponse:
        """Update Dashboard Report.

        Update a Dashboard Report configuration, including the schedule and email settings.  Changes to the schedule happen immediately, but it may take up to five minutes for your report to be sent if the scheduled time is close to the time of the update request.

        :param dashboard_id: ID of the dashboard for which to update the associated report.
        :type dashboard_id: str
        :param report_uuid: ID of the dashboard report to update.
        :type report_uuid: str
        :type body: DashboardReportUpdateRequest
        :rtype: DashboardReportResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dashboard_id"] = dashboard_id

        kwargs["report_uuid"] = report_uuid

        kwargs["body"] = body

        return self._update_dashboard_report_config_endpoint.call_with_http_info(**kwargs)
