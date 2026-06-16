# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UUID,
)
from datadog_api_client.v2.model.report_schedule_response import ReportScheduleResponse
from datadog_api_client.v2.model.report_schedule_create_request import ReportScheduleCreateRequest
from datadog_api_client.v2.model.report_schedule_patch_request import ReportSchedulePatchRequest


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
