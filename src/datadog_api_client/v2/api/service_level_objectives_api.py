# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.slo_report_post_response import SLOReportPostResponse
from datadog_api_client.v2.model.slo_report_create_request import SloReportCreateRequest
from datadog_api_client.v2.model.slo_report_status_get_response import SLOReportStatusGetResponse


class ServiceLevelObjectivesApi:
    """
    `Service Level Objectives <https://docs.datadoghq.com/monitors/service_level_objectives/#configuration>`_
    (SLOs) are a key part of the site reliability engineering toolkit.
    SLOs provide a framework for defining clear targets around application performance,
    which ultimately help teams provide a consistent customer experience,
    balance feature development with platform stability,
    and improve communication with internal and external users.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_slo_report_job_endpoint = _Endpoint(
            settings={
                "response_type": (SLOReportPostResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/slo/report",
                "operation_id": "create_slo_report_job",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SloReportCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_slo_report_endpoint = _Endpoint(
            settings={
                "response_type": (str,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/slo/report/{report_id}/download",
                "operation_id": "get_slo_report",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "report_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "report_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["text/csv", "application/json"],
            },
            api_client=api_client,
        )

        self._get_slo_report_job_status_endpoint = _Endpoint(
            settings={
                "response_type": (SLOReportStatusGetResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/slo/report/{report_id}/status",
                "operation_id": "get_slo_report_job_status",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "report_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "report_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

    def create_slo_report_job(
        self,
        body: SloReportCreateRequest,
    ) -> SLOReportPostResponse:
        """Create a new SLO report.

        Create a job to generate an SLO report. The report job is processed asynchronously and eventually results in a CSV report being available for download.

        Check the status of the job and download the CSV report using the returned ``report_id``.

        :param body: Create SLO report job request body.
        :type body: SloReportCreateRequest
        :rtype: SLOReportPostResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_slo_report_job_endpoint.call_with_http_info(**kwargs)

    def get_slo_report(
        self,
        report_id: str,
    ) -> str:
        """Get SLO report.

        Download an SLO report. This can only be performed after the report job has completed.

        Reports are not guaranteed to exist indefinitely. Datadog recommends that you download the report as soon as it is available.

        :param report_id: The ID of the report job.
        :type report_id: str
        :rtype: str
        """
        kwargs: Dict[str, Any] = {}
        kwargs["report_id"] = report_id

        return self._get_slo_report_endpoint.call_with_http_info(**kwargs)

    def get_slo_report_job_status(
        self,
        report_id: str,
    ) -> SLOReportStatusGetResponse:
        """Get SLO report status.

        Get the status of the SLO report job.

        :param report_id: The ID of the report job.
        :type report_id: str
        :rtype: SLOReportStatusGetResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["report_id"] = report_id

        return self._get_slo_report_job_status_endpoint.call_with_http_info(**kwargs)
