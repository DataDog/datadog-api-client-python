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
    Manage configuration of `RUM-based metrics <https://app.datadoghq.com/rum/generate-metrics>`_ for your organization.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_rum_metric_endpoint = _Endpoint(
            settings={
                "response_type": (RumMetricResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
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
        """Create a RUM-based metric.

        Create a metric based on your organization's RUM data.
        The metric name is set in ``data.id`` , is unique within your organization, and cannot be changed after creation.
        The ``event_type`` , ``compute`` , and ``uniqueness`` settings cannot be changed after creation either. Only ``filter`` , ``group_by`` , and ``compute.include_percentiles`` can be changed with ``UpdateRumMetric``.
        ``uniqueness`` is required when ``event_type`` is ``session`` or ``view`` , and must be omitted for any other event type.
        When ``aggregation_type`` is ``distribution`` , ``include_percentiles`` is required. When it is ``count`` , ``include_percentiles`` and ``path`` must be omitted.
        Returns the created RUM-based metric when the request is successful.
        The request returns a ``409 Conflict`` error if a metric with the same name already exists.

        :param body: The definition of the new RUM-based metric.
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
        """Delete a RUM-based metric.

        Delete a specific RUM-based metric from your organization.
        Metric data that was already generated is not deleted. Deleting a metric cannot be undone.

        :param metric_id: The name of the RUM-based metric, as returned in ``data.id`` by ``ListRumMetrics``.
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
        """Get a RUM-based metric.

        Get a specific RUM-based metric from your organization.
        The ``metric_id`` is the metric name returned in ``data.id`` by ``ListRumMetrics`` and ``CreateRumMetric``.

        :param metric_id: The name of the RUM-based metric, as returned in ``data.id`` by ``ListRumMetrics``.
        :type metric_id: str
        :rtype: RumMetricResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_id"] = metric_id

        return self._get_rum_metric_endpoint.call_with_http_info(**kwargs)

    def list_rum_metrics(
        self,
    ) -> RumMetricsResponse:
        """Get all RUM-based metrics.

        Get the list of all RUM-based metrics configured for your organization, with their definitions.
        The list is not paginated.
        Metrics whose stored definition cannot be converted to the RUM format are omitted from the list.
        To retrieve a single metric, use ``GetRumMetric``.

        :rtype: RumMetricsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_rum_metrics_endpoint.call_with_http_info(**kwargs)

    def update_rum_metric(
        self,
        metric_id: str,
        body: RumMetricUpdateRequest,
    ) -> RumMetricResponse:
        """Update a RUM-based metric.

        Update a specific RUM-based metric from your organization.
        Only ``filter`` , ``group_by`` , and ``compute.include_percentiles`` can be updated. ``event_type`` , ``uniqueness`` , ``compute.aggregation_type`` , ``compute.path`` , and the metric name are immutable. To change them, delete the metric and create a new one.
        Omitted attributes keep their current value. When provided, ``filter.query`` replaces the whole filter query (an empty query is ignored) and ``group_by`` replaces the whole list of group by rules.
        ``data.id`` is required and must match the ``metric_id`` path parameter, otherwise the request returns a ``409 Conflict`` error.
        The request also returns a ``409 Conflict`` error when ``compute.include_percentiles`` is set on a metric whose ``aggregation_type`` is not ``distribution``.
        Returns the updated RUM-based metric when the request is successful.

        :param metric_id: The name of the RUM-based metric, as returned in ``data.id`` by ``ListRumMetrics``.
        :type metric_id: str
        :param body: New definition of the RUM-based metric.
        :type body: RumMetricUpdateRequest
        :rtype: RumMetricResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_id"] = metric_id

        kwargs["body"] = body

        return self._update_rum_metric_endpoint.call_with_http_info(**kwargs)
