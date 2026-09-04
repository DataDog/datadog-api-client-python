# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.timeseries_anomaly_investigation_response import TimeseriesAnomalyInvestigationResponse
from datadog_api_client.v2.model.timeseries_anomaly_investigation_request import TimeseriesAnomalyInvestigationRequest


class TimeseriesAnomalyInvestigationsApi:
    """
    Investigate metrics timeseries anomalies and return deterministic findings.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_timeseries_anomaly_investigation_endpoint = _Endpoint(
            settings={
                "response_type": (TimeseriesAnomalyInvestigationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/timeseries-anomaly-investigations",
                "operation_id": "create_timeseries_anomaly_investigation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TimeseriesAnomalyInvestigationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_timeseries_anomaly_investigation(
        self,
        body: TimeseriesAnomalyInvestigationRequest,
    ) -> TimeseriesAnomalyInvestigationResponse:
        """Investigate a timeseries anomaly.

        Investigates a metrics timeseries request for its most significant anomaly and returns deterministic findings.
        Metrics queries with or without grouping are supported. This API version accepts exactly one request and returns at most one anomaly.

        :param body: Metrics timeseries request to investigate.
        :type body: TimeseriesAnomalyInvestigationRequest
        :rtype: TimeseriesAnomalyInvestigationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_timeseries_anomaly_investigation_endpoint.call_with_http_info(**kwargs)
