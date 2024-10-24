# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.rum_metrics_response import RumMetricsResponse
from datadog_api_client.v2.model.rum_metric_response import RumMetricResponse
from datadog_api_client.v2.model.rum_metric_create_request import RumMetricCreateRequest
from datadog_api_client.v2.model.rum_metric_update_request import RumMetricUpdateRequest


class RumMetricsApi:
    """
    Manage configuration of `rum-based metrics <https://app.datadoghq.com/rum/generate-metrics>`_ for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_metric_endpoint = _Endpoint(
            settings={
                "response_type": (RumMetricResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/metrics",
                "operation_id": "create_rum_metric",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RumMetricCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_rum_metric_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/metrics/{metric_id}",
                "operation_id": "delete_rum_metric",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "metric_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_rum_metric_endpoint = _Endpoint(
            settings={
                "response_type": (RumMetricResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/metrics/{metric_id}",
                "operation_id": "get_rum_metric",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_rum_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (RumMetricsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/metrics",
                "operation_id": "list_rum_metrics",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_rum_metric_endpoint = _Endpoint(
            settings={
                "response_type": (RumMetricResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/rum/config/metrics/{metric_id}",
                "operation_id": "update_rum_metric",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "metric_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (RumMetricUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_rum_metric(
        self,
        body: RumMetricCreateRequest,
    ) -> RumMetricResponse:
        """Create a rum-based metric.

        Create a metric based on your organization's RUM data.
        Returns the rum-based metric object from the request body when the request is successful.

        :param body: The definition of the new rum-based metric.
        :type body: RumMetricCreateRequest
        :rtype: RumMetricResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_rum_metric_endpoint.call_with_http_info(**kwargs)

    def delete_rum_metric(
        self,
        metric_id: str,
    ) -> None:
        """Delete a rum-based metric.

        Delete a specific rum-based metric from your organization.

        :param metric_id: The name of the rum-based metric.
        :type metric_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_id"] = metric_id

        return self._delete_rum_metric_endpoint.call_with_http_info(**kwargs)

    def get_rum_metric(
        self,
        metric_id: str,
    ) -> RumMetricResponse:
        """Get a rum-based metric.

        Get a specific rum-based metric from your organization.

        :param metric_id: The name of the rum-based metric.
        :type metric_id: str
        :rtype: RumMetricResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_id"] = metric_id

        return self._get_rum_metric_endpoint.call_with_http_info(**kwargs)

    def list_rum_metrics(
        self,
    ) -> RumMetricsResponse:
        """Get all rum-based metrics.

        Get the list of configured rum-based metrics with their definitions.

        :rtype: RumMetricsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_rum_metrics_endpoint.call_with_http_info(**kwargs)

    def update_rum_metric(
        self,
        metric_id: str,
        body: RumMetricUpdateRequest,
    ) -> RumMetricResponse:
        """Update a rum-based metric.

        Update a specific rum-based metric from your organization.
        Returns the rum-based metric object from the request body when the request is successful.

        :param metric_id: The name of the rum-based metric.
        :type metric_id: str
        :param body: New definition of the rum-based metric.
        :type body: RumMetricUpdateRequest
        :rtype: RumMetricResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_id"] = metric_id

        kwargs["body"] = body

        return self._update_rum_metric_endpoint.call_with_http_info(**kwargs)
