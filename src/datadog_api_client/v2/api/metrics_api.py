# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.metrics_and_metric_tag_configurations_response import (
    MetricsAndMetricTagConfigurationsResponse,
)
from datadog_api_client.v2.model.metric_tag_configuration_metric_type_category import (
    MetricTagConfigurationMetricTypeCategory,
)
from datadog_api_client.v2.model.metrics_and_metric_tag_configurations import MetricsAndMetricTagConfigurations
from datadog_api_client.v2.model.metric_bulk_tag_config_response import MetricBulkTagConfigResponse
from datadog_api_client.v2.model.metric_bulk_tag_config_delete_request import MetricBulkTagConfigDeleteRequest
from datadog_api_client.v2.model.metric_bulk_tag_config_create_request import MetricBulkTagConfigCreateRequest
from datadog_api_client.v2.model.metric_suggested_tags_and_aggregations_response import (
    MetricSuggestedTagsAndAggregationsResponse,
)
from datadog_api_client.v2.model.metric_all_tags_response import MetricAllTagsResponse
from datadog_api_client.v2.model.metric_assets_response import MetricAssetsResponse
from datadog_api_client.v2.model.metric_estimate_response import MetricEstimateResponse
from datadog_api_client.v2.model.metric_tag_cardinalities_response import MetricTagCardinalitiesResponse
from datadog_api_client.v2.model.metric_tag_configuration_response import MetricTagConfigurationResponse
from datadog_api_client.v2.model.metric_tag_configuration_update_request import MetricTagConfigurationUpdateRequest
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequest
from datadog_api_client.v2.model.metric_volumes_response import MetricVolumesResponse
from datadog_api_client.v2.model.scalar_formula_query_response import ScalarFormulaQueryResponse
from datadog_api_client.v2.model.scalar_formula_query_request import ScalarFormulaQueryRequest
from datadog_api_client.v2.model.timeseries_formula_query_response import TimeseriesFormulaQueryResponse
from datadog_api_client.v2.model.timeseries_formula_query_request import TimeseriesFormulaQueryRequest
from datadog_api_client.v2.model.intake_payload_accepted import IntakePayloadAccepted
from datadog_api_client.v2.model.metric_content_encoding import MetricContentEncoding
from datadog_api_client.v2.model.metric_payload import MetricPayload


class MetricsApi:
    """
    The metrics endpoint allows you to:

    * Post metrics data so it can be graphed on Datadog’s dashboards
    * Query metrics from any time period (timeseries and scalar)
    * Modify tag configurations for metrics
    * View tags and volumes for metrics

    **Note** : A graph can only contain a set number of points
    and as the timeframe over which a metric is viewed increases,
    aggregation between points occurs to stay below that set number.

    The Post, Patch, and Delete ``manage_tags`` API methods can only be performed by
    a user who has the ``Manage Tags for Metrics`` permission.

    See the `Metrics page <https://docs.datadoghq.com/metrics/>`_ for more information.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_bulk_tags_metrics_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (MetricBulkTagConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/config/bulk-tags",
                "operation_id": "create_bulk_tags_metrics_configuration",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MetricBulkTagConfigCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_tag_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (MetricTagConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "create_tag_configuration",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MetricTagConfigurationCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_bulk_tags_metrics_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (MetricBulkTagConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/config/bulk-tags",
                "operation_id": "delete_bulk_tags_metrics_configuration",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (MetricBulkTagConfigDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_tag_configuration_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "delete_tag_configuration",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._estimate_metrics_output_series_endpoint = _Endpoint(
            settings={
                "response_type": (MetricEstimateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/estimate",
                "operation_id": "estimate_metrics_output_series",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
                "filter_groups": {
                    "openapi_types": (str,),
                    "attribute": "filter[groups]",
                    "location": "query",
                },
                "filter_hours_ago": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                        "inclusive_minimum": 49,
                    },
                    "openapi_types": (int,),
                    "attribute": "filter[hours_ago]",
                    "location": "query",
                },
                "filter_num_aggregations": {
                    "validation": {
                        "inclusive_maximum": 9,
                    },
                    "openapi_types": (int,),
                    "attribute": "filter[num_aggregations]",
                    "location": "query",
                },
                "filter_pct": {
                    "openapi_types": (bool,),
                    "attribute": "filter[pct]",
                    "location": "query",
                },
                "filter_timespan_h": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                    },
                    "openapi_types": (int,),
                    "attribute": "filter[timespan_h]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_metric_tag_cardinality_details_endpoint = _Endpoint(
            settings={
                "response_type": (MetricTagCardinalitiesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tag-cardinalities",
                "operation_id": "get_metric_tag_cardinality_details",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_active_metric_configurations_endpoint = _Endpoint(
            settings={
                "response_type": (MetricSuggestedTagsAndAggregationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/active-configurations",
                "operation_id": "list_active_metric_configurations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
                "window_seconds": {
                    "openapi_types": (int,),
                    "attribute": "window[seconds]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_metric_assets_endpoint = _Endpoint(
            settings={
                "response_type": (MetricAssetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/assets",
                "operation_id": "list_metric_assets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_tag_configuration_by_name_endpoint = _Endpoint(
            settings={
                "response_type": (MetricTagConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "list_tag_configuration_by_name",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_tag_configurations_endpoint = _Endpoint(
            settings={
                "response_type": (MetricsAndMetricTagConfigurationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/metrics",
                "operation_id": "list_tag_configurations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_configured": {
                    "openapi_types": (bool,),
                    "attribute": "filter[configured]",
                    "location": "query",
                },
                "filter_tags_configured": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags_configured]",
                    "location": "query",
                },
                "filter_metric_type": {
                    "openapi_types": (MetricTagConfigurationMetricTypeCategory,),
                    "attribute": "filter[metric_type]",
                    "location": "query",
                },
                "filter_include_percentiles": {
                    "openapi_types": (bool,),
                    "attribute": "filter[include_percentiles]",
                    "location": "query",
                },
                "filter_queried": {
                    "openapi_types": (bool,),
                    "attribute": "filter[queried]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "filter_related_assets": {
                    "openapi_types": (bool,),
                    "attribute": "filter[related_assets]",
                    "location": "query",
                },
                "window_seconds": {
                    "openapi_types": (int,),
                    "attribute": "window[seconds]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 10000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_tags_by_metric_name_endpoint = _Endpoint(
            settings={
                "response_type": (MetricAllTagsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/all-tags",
                "operation_id": "list_tags_by_metric_name",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_volumes_by_metric_name_endpoint = _Endpoint(
            settings={
                "response_type": (MetricVolumesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/volumes",
                "operation_id": "list_volumes_by_metric_name",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._query_scalar_data_endpoint = _Endpoint(
            settings={
                "response_type": (ScalarFormulaQueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/query/scalar",
                "operation_id": "query_scalar_data",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ScalarFormulaQueryRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._query_timeseries_data_endpoint = _Endpoint(
            settings={
                "response_type": (TimeseriesFormulaQueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/query/timeseries",
                "operation_id": "query_timeseries_data",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (TimeseriesFormulaQueryRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._submit_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (IntakePayloadAccepted,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/series",
                "operation_id": "submit_metrics",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "content_encoding": {
                    "openapi_types": (MetricContentEncoding,),
                    "attribute": "Content-Encoding",
                    "location": "header",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MetricPayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_tag_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (MetricTagConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "update_tag_configuration",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "metric_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "metric_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MetricTagConfigurationUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_bulk_tags_metrics_configuration(
        self,
        body: MetricBulkTagConfigCreateRequest,
    ) -> MetricBulkTagConfigResponse:
        """Configure tags for multiple metrics.

        Create and define a list of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.
        Metrics are selected by passing a metric name prefix. Use the Delete method of this API path to remove tag configurations.
        Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app.
        If multiple calls include the same metric, the last configuration applied (not by submit order) is used, do not
        expect deterministic ordering of concurrent calls. The ``exclude_tags_mode`` value will set all metrics that match the prefix to
        the same exclusion state, metric tag configurations do not support mixed inclusion and exclusion for tags on the same metric.
        Can only be used with application keys of users with the ``Manage Tags for Metrics`` permission.

        :type body: MetricBulkTagConfigCreateRequest
        :rtype: MetricBulkTagConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_bulk_tags_metrics_configuration_endpoint.call_with_http_info(**kwargs)

    def create_tag_configuration(
        self,
        metric_name: str,
        body: MetricTagConfigurationCreateRequest,
    ) -> MetricTagConfigurationResponse:
        """Create a tag configuration.

        Create and define a list of queryable tag keys for an existing count/gauge/rate/distribution metric.
        Optionally, include percentile aggregations on any distribution metric. By setting ``exclude_tags_mode``
        to true, the behavior is changed from an allow-list to a deny-list, and tags in the defined list are
        not queryable. Can only be used with application keys of users with the ``Manage Tags for Metrics``
        permission.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :type body: MetricTagConfigurationCreateRequest
        :rtype: MetricTagConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        kwargs["body"] = body

        return self._create_tag_configuration_endpoint.call_with_http_info(**kwargs)

    def delete_bulk_tags_metrics_configuration(
        self,
        body: MetricBulkTagConfigDeleteRequest,
    ) -> MetricBulkTagConfigResponse:
        """Delete tags for multiple metrics.

        Delete all custom lists of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.
        Metrics are selected by passing a metric name prefix.
        Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app.
        Can only be used with application keys of users with the ``Manage Tags for Metrics`` permission.

        :type body: MetricBulkTagConfigDeleteRequest
        :rtype: MetricBulkTagConfigResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_bulk_tags_metrics_configuration_endpoint.call_with_http_info(**kwargs)

    def delete_tag_configuration(
        self,
        metric_name: str,
    ) -> None:
        """Delete a tag configuration.

        Deletes a metric's tag configuration. Can only be used with application
        keys from users with the ``Manage Tags for Metrics`` permission.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        return self._delete_tag_configuration_endpoint.call_with_http_info(**kwargs)

    def estimate_metrics_output_series(
        self,
        metric_name: str,
        *,
        filter_groups: Union[str, UnsetType] = unset,
        filter_hours_ago: Union[int, UnsetType] = unset,
        filter_num_aggregations: Union[int, UnsetType] = unset,
        filter_pct: Union[bool, UnsetType] = unset,
        filter_timespan_h: Union[int, UnsetType] = unset,
    ) -> MetricEstimateResponse:
        """Tag Configuration Cardinality Estimator.

        Returns the estimated cardinality for a metric with a given tag, percentile and number of aggregations configuration using Metrics without Limits&trade;.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :param filter_groups: Filtered tag keys that the metric is configured to query with.
        :type filter_groups: str, optional
        :param filter_hours_ago: The number of hours of look back (from now) to estimate cardinality with. If unspecified, it defaults to 0 hours.
        :type filter_hours_ago: int, optional
        :param filter_num_aggregations: Deprecated. Number of aggregations has no impact on volume.
        :type filter_num_aggregations: int, optional
        :param filter_pct: A boolean, for distribution metrics only, to estimate cardinality if the metric includes additional percentile aggregators.
        :type filter_pct: bool, optional
        :param filter_timespan_h: A window, in hours, from the look back to estimate cardinality with. The minimum and default is 1 hour.
        :type filter_timespan_h: int, optional
        :rtype: MetricEstimateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        if filter_groups is not unset:
            kwargs["filter_groups"] = filter_groups

        if filter_hours_ago is not unset:
            kwargs["filter_hours_ago"] = filter_hours_ago

        if filter_num_aggregations is not unset:
            kwargs["filter_num_aggregations"] = filter_num_aggregations

        if filter_pct is not unset:
            kwargs["filter_pct"] = filter_pct

        if filter_timespan_h is not unset:
            kwargs["filter_timespan_h"] = filter_timespan_h

        return self._estimate_metrics_output_series_endpoint.call_with_http_info(**kwargs)

    def get_metric_tag_cardinality_details(
        self,
        metric_name: str,
    ) -> MetricTagCardinalitiesResponse:
        """Get tag key cardinality details.

        Returns the cardinality details of tags for a specific metric.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :rtype: MetricTagCardinalitiesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        return self._get_metric_tag_cardinality_details_endpoint.call_with_http_info(**kwargs)

    def list_active_metric_configurations(
        self,
        metric_name: str,
        *,
        window_seconds: Union[int, UnsetType] = unset,
    ) -> MetricSuggestedTagsAndAggregationsResponse:
        """List active tags and aggregations.

        List tags and aggregations that are actively queried on dashboards, notebooks, monitors, the Metrics Explorer, and using the API for a given metric name.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :param window_seconds: The number of seconds of look back (from now).
            Default value is 604,800 (1 week), minimum value is 7200 (2 hours), maximum value is 2,630,000 (1 month).
        :type window_seconds: int, optional
        :rtype: MetricSuggestedTagsAndAggregationsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        if window_seconds is not unset:
            kwargs["window_seconds"] = window_seconds

        return self._list_active_metric_configurations_endpoint.call_with_http_info(**kwargs)

    def list_metric_assets(
        self,
        metric_name: str,
    ) -> MetricAssetsResponse:
        """Related Assets to a Metric.

        Returns dashboards, monitors, notebooks, and SLOs that a metric is stored in, if any.  Updated every 24 hours.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :rtype: MetricAssetsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        return self._list_metric_assets_endpoint.call_with_http_info(**kwargs)

    def list_tag_configuration_by_name(
        self,
        metric_name: str,
    ) -> MetricTagConfigurationResponse:
        """List tag configuration by name.

        Returns the tag configuration for the given metric name.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :rtype: MetricTagConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        return self._list_tag_configuration_by_name_endpoint.call_with_http_info(**kwargs)

    def list_tag_configurations(
        self,
        *,
        filter_configured: Union[bool, UnsetType] = unset,
        filter_tags_configured: Union[str, UnsetType] = unset,
        filter_metric_type: Union[MetricTagConfigurationMetricTypeCategory, UnsetType] = unset,
        filter_include_percentiles: Union[bool, UnsetType] = unset,
        filter_queried: Union[bool, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_related_assets: Union[bool, UnsetType] = unset,
        window_seconds: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> MetricsAndMetricTagConfigurationsResponse:
        """Get a list of metrics.

        Returns all metrics that can be configured in the Metrics Summary page or with Metrics without Limits™ (matching additional filters if specified).
        Optionally, paginate by using the ``page[cursor]`` and/or ``page[size]`` query parameters.
        To fetch the first page, pass in a query parameter with either a valid ``page[size]`` or an empty cursor like ``page[cursor]=``. To fetch the next page, pass in the ``next_cursor`` value from the response as the new ``page[cursor]`` value.
        Once the ``meta.pagination.next_cursor`` value is null, all pages have been retrieved.

        :param filter_configured: Filter custom metrics that have configured tags.
        :type filter_configured: bool, optional
        :param filter_tags_configured: Filter tag configurations by configured tags.
        :type filter_tags_configured: str, optional
        :param filter_metric_type: Filter metrics by metric type.
        :type filter_metric_type: MetricTagConfigurationMetricTypeCategory, optional
        :param filter_include_percentiles: Filter distributions with additional percentile
            aggregations enabled or disabled.
        :type filter_include_percentiles: bool, optional
        :param filter_queried: (Preview) Filter custom metrics that have or have not been queried in the specified window[seconds].
            If no window is provided or the window is less than 2 hours, a default of 2 hours will be applied.
        :type filter_queried: bool, optional
        :param filter_tags: Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions.
            Can only be combined with the filter[queried] filter.
        :type filter_tags: str, optional
        :param filter_related_assets: (Preview) Filter metrics that are used in dashboards, monitors, notebooks, SLOs.
        :type filter_related_assets: bool, optional
        :param window_seconds: The number of seconds of look back (from now) to apply to a filter[tag] or filter[queried] query.
            Default value is 3600 (1 hour), maximum value is 2,592,000 (30 days).
        :type window_seconds: int, optional
        :param page_size: Maximum number of results returned.
        :type page_size: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in ``meta.pagination.next_cursor``.
            Once the ``meta.pagination.next_cursor`` key is null, all pages have been retrieved.
        :type page_cursor: str, optional
        :rtype: MetricsAndMetricTagConfigurationsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_configured is not unset:
            kwargs["filter_configured"] = filter_configured

        if filter_tags_configured is not unset:
            kwargs["filter_tags_configured"] = filter_tags_configured

        if filter_metric_type is not unset:
            kwargs["filter_metric_type"] = filter_metric_type

        if filter_include_percentiles is not unset:
            kwargs["filter_include_percentiles"] = filter_include_percentiles

        if filter_queried is not unset:
            kwargs["filter_queried"] = filter_queried

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_related_assets is not unset:
            kwargs["filter_related_assets"] = filter_related_assets

        if window_seconds is not unset:
            kwargs["window_seconds"] = window_seconds

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        return self._list_tag_configurations_endpoint.call_with_http_info(**kwargs)

    def list_tag_configurations_with_pagination(
        self,
        *,
        filter_configured: Union[bool, UnsetType] = unset,
        filter_tags_configured: Union[str, UnsetType] = unset,
        filter_metric_type: Union[MetricTagConfigurationMetricTypeCategory, UnsetType] = unset,
        filter_include_percentiles: Union[bool, UnsetType] = unset,
        filter_queried: Union[bool, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_related_assets: Union[bool, UnsetType] = unset,
        window_seconds: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[MetricsAndMetricTagConfigurations]:
        """Get a list of metrics.

        Provide a paginated version of :meth:`list_tag_configurations`, returning all items.

        :param filter_configured: Filter custom metrics that have configured tags.
        :type filter_configured: bool, optional
        :param filter_tags_configured: Filter tag configurations by configured tags.
        :type filter_tags_configured: str, optional
        :param filter_metric_type: Filter metrics by metric type.
        :type filter_metric_type: MetricTagConfigurationMetricTypeCategory, optional
        :param filter_include_percentiles: Filter distributions with additional percentile
            aggregations enabled or disabled.
        :type filter_include_percentiles: bool, optional
        :param filter_queried: (Preview) Filter custom metrics that have or have not been queried in the specified window[seconds].
            If no window is provided or the window is less than 2 hours, a default of 2 hours will be applied.
        :type filter_queried: bool, optional
        :param filter_tags: Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions.
            Can only be combined with the filter[queried] filter.
        :type filter_tags: str, optional
        :param filter_related_assets: (Preview) Filter metrics that are used in dashboards, monitors, notebooks, SLOs.
        :type filter_related_assets: bool, optional
        :param window_seconds: The number of seconds of look back (from now) to apply to a filter[tag] or filter[queried] query.
            Default value is 3600 (1 hour), maximum value is 2,592,000 (30 days).
        :type window_seconds: int, optional
        :param page_size: Maximum number of results returned.
        :type page_size: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in ``meta.pagination.next_cursor``.
            Once the ``meta.pagination.next_cursor`` key is null, all pages have been retrieved.
        :type page_cursor: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[MetricsAndMetricTagConfigurations]
        """
        kwargs: Dict[str, Any] = {}
        if filter_configured is not unset:
            kwargs["filter_configured"] = filter_configured

        if filter_tags_configured is not unset:
            kwargs["filter_tags_configured"] = filter_tags_configured

        if filter_metric_type is not unset:
            kwargs["filter_metric_type"] = filter_metric_type

        if filter_include_percentiles is not unset:
            kwargs["filter_include_percentiles"] = filter_include_percentiles

        if filter_queried is not unset:
            kwargs["filter_queried"] = filter_queried

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_related_assets is not unset:
            kwargs["filter_related_assets"] = filter_related_assets

        if window_seconds is not unset:
            kwargs["window_seconds"] = window_seconds

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10000)
        endpoint = self._list_tag_configurations_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.pagination.next_cursor",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_tags_by_metric_name(
        self,
        metric_name: str,
    ) -> MetricAllTagsResponse:
        """List tags by metric name.

        View indexed tag key-value pairs for a given metric name over the previous hour.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :rtype: MetricAllTagsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        return self._list_tags_by_metric_name_endpoint.call_with_http_info(**kwargs)

    def list_volumes_by_metric_name(
        self,
        metric_name: str,
    ) -> MetricVolumesResponse:
        """List distinct metric volumes by metric name.

        View distinct metrics volumes for the given metric name.

        Custom metrics generated in-app from other products will return ``null`` for ingested volumes.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :rtype: MetricVolumesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        return self._list_volumes_by_metric_name_endpoint.call_with_http_info(**kwargs)

    def query_scalar_data(
        self,
        body: ScalarFormulaQueryRequest,
    ) -> ScalarFormulaQueryResponse:
        """Query scalar data across multiple products.

        Query scalar values (as seen on Query Value, Table, and Toplist widgets).
        Multiple data sources are supported with the ability to
        process the data using formulas and functions.

        :type body: ScalarFormulaQueryRequest
        :rtype: ScalarFormulaQueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_scalar_data_endpoint.call_with_http_info(**kwargs)

    def query_timeseries_data(
        self,
        body: TimeseriesFormulaQueryRequest,
    ) -> TimeseriesFormulaQueryResponse:
        """Query timeseries data across multiple products.

        Query timeseries data across various data sources and
        process the data by applying formulas and functions.

        :type body: TimeseriesFormulaQueryRequest
        :rtype: TimeseriesFormulaQueryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._query_timeseries_data_endpoint.call_with_http_info(**kwargs)

    def submit_metrics(
        self,
        body: MetricPayload,
        *,
        content_encoding: Union[MetricContentEncoding, UnsetType] = unset,
    ) -> IntakePayloadAccepted:
        """Submit metrics.

        The metrics end-point allows you to post time-series data that can be graphed on Datadog’s dashboards.
        The maximum payload size is 500 kilobytes (512000 bytes). Compressed payloads must have a decompressed size of less than 5 megabytes (5242880 bytes).

        If you’re submitting metrics directly to the Datadog API without using DogStatsD, expect:

        * 64 bits for the timestamp
        * 64 bits for the value
        * 20 bytes for the metric names
        * 50 bytes for the timeseries
        * The full payload is approximately 100 bytes.

        Host name is one of the resources in the Resources field.

        :type body: MetricPayload
        :param content_encoding: HTTP header used to compress the media-type.
        :type content_encoding: MetricContentEncoding, optional
        :rtype: IntakePayloadAccepted
        """
        kwargs: Dict[str, Any] = {}
        if content_encoding is not unset:
            kwargs["content_encoding"] = content_encoding

        kwargs["body"] = body

        return self._submit_metrics_endpoint.call_with_http_info(**kwargs)

    def update_tag_configuration(
        self,
        metric_name: str,
        body: MetricTagConfigurationUpdateRequest,
    ) -> MetricTagConfigurationResponse:
        """Update a tag configuration.

        Update the tag configuration of a metric or percentile aggregations of a distribution metric or custom aggregations
        of a count, rate, or gauge metric. By setting ``exclude_tags_mode`` to true the behavior is changed
        from an allow-list to a deny-list, and tags in the defined list will not be queryable.
        Can only be used with application keys from users with the ``Manage Tags for Metrics`` permission. This endpoint requires
        a tag configuration to be created first.

        :param metric_name: The name of the metric.
        :type metric_name: str
        :type body: MetricTagConfigurationUpdateRequest
        :rtype: MetricTagConfigurationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_name"] = metric_name

        kwargs["body"] = body

        return self._update_tag_configuration_endpoint.call_with_http_info(**kwargs)
