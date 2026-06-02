# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.aggregated_long_tasks_response import AggregatedLongTasksResponse
from datadog_api_client.v2.model.aggregated_long_tasks_request import AggregatedLongTasksRequest
from datadog_api_client.v2.model.aggregated_signals_problems_response import AggregatedSignalsProblemsResponse
from datadog_api_client.v2.model.aggregated_signals_problems_request import AggregatedSignalsProblemsRequest
from datadog_api_client.v2.model.aggregated_waterfall_response import AggregatedWaterfallResponse
from datadog_api_client.v2.model.aggregated_waterfall_request import AggregatedWaterfallRequest


class RUMInsightsApi:
    """
    Get insights into the performance of your Real User Monitoring (RUM) applications over HTTP. See the `RUM & Session Replay page <https://docs.datadoghq.com/real_user_monitoring/>`_ for more information
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._query_aggregated_long_tasks_endpoint = _Endpoint(
            settings={
                "response_type": (AggregatedLongTasksResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/query/insight/aggregated_long_tasks",
                "operation_id": "query_aggregated_long_tasks",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AggregatedLongTasksRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_aggregated_signals_problems_endpoint = _Endpoint(
            settings={
                "response_type": (AggregatedSignalsProblemsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/query/insight/aggregated_signals_problems",
                "operation_id": "query_aggregated_signals_problems",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AggregatedSignalsProblemsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_aggregated_waterfall_endpoint = _Endpoint(
            settings={
                "response_type": (AggregatedWaterfallResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/query/insight/aggregated_waterfall",
                "operation_id": "query_aggregated_waterfall",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (AggregatedWaterfallRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def query_aggregated_long_tasks(
        self,
        body: AggregatedLongTasksRequest,
    ) -> AggregatedLongTasksResponse:
        """Query aggregated long tasks.

        Get aggregated long task data for a RUM view, grouped by invoker type and sampled across multiple view instances.

        :type body: AggregatedLongTasksRequest
        :rtype: AggregatedLongTasksResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_aggregated_long_tasks_endpoint.call_with_http_info(**kwargs)

    def query_aggregated_signals_problems(
        self,
        body: AggregatedSignalsProblemsRequest,
    ) -> AggregatedSignalsProblemsResponse:
        """Query aggregated signals and problems.

        Get aggregated performance signals and problem detections for a RUM view, sampled across multiple view instances.

        :type body: AggregatedSignalsProblemsRequest
        :rtype: AggregatedSignalsProblemsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_aggregated_signals_problems_endpoint.call_with_http_info(**kwargs)

    def query_aggregated_waterfall(
        self,
        body: AggregatedWaterfallRequest,
    ) -> AggregatedWaterfallResponse:
        """Query aggregated waterfall.

        Get aggregated network resource waterfall data for a RUM view, sampled across multiple view instances.

        :type body: AggregatedWaterfallRequest
        :rtype: AggregatedWaterfallResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_aggregated_waterfall_endpoint.call_with_http_info(**kwargs)
