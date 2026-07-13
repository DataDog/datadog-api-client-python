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
    UUID,
)
from datadog_api_client.v2.model.dataset_report_schedule_list_response import DatasetReportScheduleListResponse
from datadog_api_client.v2.model.print_report_response import PrintReportResponse
from datadog_api_client.v2.model.print_report_request import PrintReportRequest
from datadog_api_client.v2.model.report_schedule_response import ReportScheduleResponse
from datadog_api_client.v2.model.report_schedule_create_request import ReportScheduleCreateRequest
from datadog_api_client.v2.model.report_schedule_list_response import ReportScheduleListResponse
from datadog_api_client.v2.model.report_schedule_resource_type import ReportScheduleResourceType
from datadog_api_client.v2.model.report_schedule_patch_request import ReportSchedulePatchRequest
from datadog_api_client.v2.model.report_schedule_toggle_request import ReportScheduleToggleRequest


class ReportSchedulesApi:
    """
    Create and manage scheduled reports. A scheduled report renders a dashboard or integration
    dashboard on a recurring cadence and delivers it to a set of recipients over email, Slack,
    or Microsoft Teams.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_report_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (ReportScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/schedule",
                "operation_id": "create_report_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ReportScheduleCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_report_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (ReportScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/schedule/{schedule_uuid}",
                "operation_id": "delete_report_schedule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "schedule_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "schedule_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_report_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (ReportScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/schedule/{schedule_uuid}",
                "operation_id": "get_report_schedule",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "schedule_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "schedule_uuid",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_report_schedules_for_resource_endpoint = _Endpoint(
            settings={
                "response_type": (ReportScheduleListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/schedule/{resource_type}/{resource_id}",
                "operation_id": "get_report_schedules_for_resource",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "resource_type": {
                    "required": True,
                    "openapi_types": (ReportScheduleResourceType,),
                    "attribute": "resource_type",
                    "location": "path",
                },
                "resource_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "resource_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_dataset_report_schedules_endpoint = _Endpoint(
            settings={
                "response_type": (DatasetReportScheduleListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/dataset/{dataset_id}/schedules",
                "operation_id": "list_dataset_report_schedules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "dataset_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dataset_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_report_schedules_endpoint = _Endpoint(
            settings={
                "response_type": (ReportScheduleListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/schedule/list",
                "operation_id": "list_report_schedules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 50,
                        "inclusive_minimum": 1,
                    },
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
                "filter_title": {
                    "openapi_types": (str,),
                    "attribute": "filter[title]",
                    "location": "query",
                },
                "filter_author_uuid": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[author_uuid]",
                    "location": "query",
                },
                "filter_recipients": {
                    "openapi_types": (str,),
                    "attribute": "filter[recipients]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._patch_report_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (ReportScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/schedule/{schedule_uuid}",
                "operation_id": "patch_report_schedule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "schedule_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "schedule_uuid",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ReportSchedulePatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._print_report_endpoint = _Endpoint(
            settings={
                "response_type": (PrintReportResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/print",
                "operation_id": "print_report",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (PrintReportRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._toggle_report_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (ReportScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/reporting/schedule/{schedule_uuid}/toggle",
                "operation_id": "toggle_report_schedule",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "schedule_uuid": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "schedule_uuid",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ReportScheduleToggleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_report_schedule(
        self,
        body: ReportScheduleCreateRequest,
    ) -> ReportScheduleResponse:
        """Create a report schedule.

        Create a new scheduled report. A schedule renders a dashboard or integration dashboard
        on a recurring cadence and delivers it to the configured recipients over email, Slack,
        or Microsoft Teams.
        Requires the ``generate_dashboard_reports`` permission.

        :type body: ReportScheduleCreateRequest
        :rtype: ReportScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_report_schedule_endpoint.call_with_http_info(**kwargs)

    def delete_report_schedule(
        self,
        schedule_uuid: UUID,
    ) -> ReportScheduleResponse:
        """Delete a report schedule.

        Delete a report schedule by its unique identifier. The response returns the deleted schedule.
        Requires a reporting write permission appropriate to the targeted resource type and schedule ownership.

        :param schedule_uuid: The unique identifier of the report schedule to delete.
        :type schedule_uuid: UUID
        :rtype: ReportScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["schedule_uuid"] = schedule_uuid

        return self._delete_report_schedule_endpoint.call_with_http_info(**kwargs)

    def get_report_schedule(
        self,
        schedule_uuid: UUID,
    ) -> ReportScheduleResponse:
        """Get a report schedule.

        Get a report schedule by its unique identifier.
        Requires a reporting read permission appropriate to the targeted resource type.

        :param schedule_uuid: The unique identifier of the report schedule to fetch.
        :type schedule_uuid: UUID
        :rtype: ReportScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["schedule_uuid"] = schedule_uuid

        return self._get_report_schedule_endpoint.call_with_http_info(**kwargs)

    def get_report_schedules_for_resource(
        self,
        resource_type: ReportScheduleResourceType,
        resource_id: str,
    ) -> ReportScheduleListResponse:
        """Get report schedules for a resource.

        Get all report schedules that target a dashboard or integration dashboard resource.
        Requires a reporting read permission appropriate to the targeted resource type.

        :param resource_type: The type of resource to fetch report schedules for.
        :type resource_type: ReportScheduleResourceType
        :param resource_id: The identifier of the resource to fetch report schedules for.
        :type resource_id: str
        :rtype: ReportScheduleListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["resource_type"] = resource_type

        kwargs["resource_id"] = resource_id

        return self._get_report_schedules_for_resource_endpoint.call_with_http_info(**kwargs)

    def list_dataset_report_schedules(
        self,
        dataset_id: str,
    ) -> DatasetReportScheduleListResponse:
        """List dataset report schedules.

        Retrieve all report schedules for a given published dataset.
        Returns report schedules belonging to the authenticated user's organization that target the specified dataset.
        Requires the ``generate_log_reports`` or ``manage_log_reports`` permission.

        :param dataset_id: The identifier of the published dataset to retrieve report schedules for.
        :type dataset_id: str
        :rtype: DatasetReportScheduleListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["dataset_id"] = dataset_id

        return self._list_dataset_report_schedules_endpoint.call_with_http_info(**kwargs)

    def list_report_schedules(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        filter_title: Union[str, UnsetType] = unset,
        filter_author_uuid: Union[UUID, UnsetType] = unset,
        filter_recipients: Union[str, UnsetType] = unset,
    ) -> ReportScheduleListResponse:
        """List report schedules.

        List dashboard and integration dashboard report schedules for the organization.
        The response is paginated and can be filtered by title, author UUID, or recipients.
        Requires the ``generate_dashboard_reports`` permission.

        :param page_limit: The maximum number of schedules to return. The maximum value is 50.
        :type page_limit: int, optional
        :param page_offset: The offset from which to start returning schedules.
        :type page_offset: int, optional
        :param filter_title: Filter schedules by report title.
        :type filter_title: str, optional
        :param filter_author_uuid: Filter schedules by author UUID.
        :type filter_author_uuid: UUID, optional
        :param filter_recipients: Filter schedules by a comma-separated list of recipients.
        :type filter_recipients: str, optional
        :rtype: ReportScheduleListResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if filter_title is not unset:
            kwargs["filter_title"] = filter_title

        if filter_author_uuid is not unset:
            kwargs["filter_author_uuid"] = filter_author_uuid

        if filter_recipients is not unset:
            kwargs["filter_recipients"] = filter_recipients

        return self._list_report_schedules_endpoint.call_with_http_info(**kwargs)

    def patch_report_schedule(
        self,
        schedule_uuid: UUID,
        body: ReportSchedulePatchRequest,
    ) -> ReportScheduleResponse:
        """Update a report schedule.

        Update an existing scheduled report by its identifier. The editable attributes
        are replaced with the supplied values; the targeted resource ( ``resource_id`` and
        ``resource_type`` ) cannot be changed after creation.
        Requires the ``generate_dashboard_reports`` permission and schedule ownership.

        :param schedule_uuid: The unique identifier of the report schedule to update.
        :type schedule_uuid: UUID
        :type body: ReportSchedulePatchRequest
        :rtype: ReportScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["schedule_uuid"] = schedule_uuid

        kwargs["body"] = body

        return self._patch_report_schedule_endpoint.call_with_http_info(**kwargs)

    def print_report(
        self,
        body: PrintReportRequest,
    ) -> PrintReportResponse:
        """Print a report.

        Initiate a one-off, print-only report for a dashboard or integration dashboard.
        The report is rendered as a PDF and made available for download through the URL returned in the response.
        Requires a reporting permission appropriate to the targeted resource type.

        :type body: PrintReportRequest
        :rtype: PrintReportResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._print_report_endpoint.call_with_http_info(**kwargs)

    def toggle_report_schedule(
        self,
        schedule_uuid: UUID,
        body: ReportScheduleToggleRequest,
    ) -> ReportScheduleResponse:
        """Toggle a report schedule.

        Activate or pause a report schedule by setting its status to ``active`` or ``inactive``.
        Requires a reporting write permission appropriate to the targeted resource type and schedule ownership.

        :param schedule_uuid: The unique identifier of the report schedule to toggle.
        :type schedule_uuid: UUID
        :type body: ReportScheduleToggleRequest
        :rtype: ReportScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["schedule_uuid"] = schedule_uuid

        kwargs["body"] = body

        return self._toggle_report_schedule_endpoint.call_with_http_info(**kwargs)
