# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.metrics_and_metric_tag_configurations_response import (
    MetricsAndMetricTagConfigurationsResponse,
)
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes
from datadog_api_client.v2.model.metric_bulk_tag_config_response import MetricBulkTagConfigResponse
from datadog_api_client.v2.model.metric_bulk_tag_config_delete_request import MetricBulkTagConfigDeleteRequest
from datadog_api_client.v2.model.metric_bulk_tag_config_create_request import MetricBulkTagConfigCreateRequest
from datadog_api_client.v2.model.metric_all_tags_response import MetricAllTagsResponse
from datadog_api_client.v2.model.metric_tag_configuration_response import MetricTagConfigurationResponse
from datadog_api_client.v2.model.metric_tag_configuration_update_request import MetricTagConfigurationUpdateRequest
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequest
from datadog_api_client.v2.model.metric_volumes_response import MetricVolumesResponse


class MetricsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_bulk_tags_metrics_configuration_endpoint = _Endpoint(
            settings={
                "response_type": (MetricBulkTagConfigResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/config/bulk-tags",
                "operation_id": "create_bulk_tags_metrics_configuration",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
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
                "servers": None,
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
                "servers": None,
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
                "servers": None,
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
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_tag_configuration_by_name_endpoint = _Endpoint(
            settings={
                "response_type": (MetricTagConfigurationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/tags",
                "operation_id": "list_tag_configuration_by_name",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
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
                "content_type": [],
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
                "servers": None,
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
                    "openapi_types": (MetricTagConfigurationMetricTypes,),
                    "attribute": "filter[metric_type]",
                    "location": "query",
                },
                "filter_include_percentiles": {
                    "openapi_types": (bool,),
                    "attribute": "filter[include_percentiles]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "window_seconds": {
                    "openapi_types": (int,),
                    "attribute": "window[seconds]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
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
                "servers": None,
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
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_volumes_by_metric_name_endpoint = _Endpoint(
            settings={
                "response_type": (MetricVolumesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/metrics/{metric_name}/volumes",
                "operation_id": "list_volumes_by_metric_name",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
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
                "content_type": [],
            },
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
                "servers": None,
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

    def create_bulk_tags_metrics_configuration(self, body, **kwargs):
        """Configure tags for multiple metrics.

        Create and define a list of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.
        Metrics are selected by passing a metric name prefix. Use the Delete method of this API path to remove tag configurations.
        Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app.
        If multiple calls include the same metric, the last configuration applied (not by submit order) is used, do not
        expect deterministic ordering of concurrent calls.
        Can only be used with application keys of users with the `Manage Tags for Metrics` permission.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_bulk_tags_metrics_configuration(body, async_req=True)
        >>> result = thread.get()

        :type body: MetricBulkTagConfigCreateRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricBulkTagConfigResponse
        """
        kwargs = self._create_bulk_tags_metrics_configuration_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_bulk_tags_metrics_configuration_endpoint.call_with_http_info(**kwargs)

    def create_tag_configuration(self, metric_name, body, **kwargs):
        """Create a tag configuration.

        Create and define a list of queryable tag keys for an existing count/gauge/rate/distribution metric.
        Optionally, include percentile aggregations on any distribution metric or configure custom aggregations
        on any count, rate, or gauge metric.
        Can only be used with application keys of users with the `Manage Tags for Metrics` permission.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_tag_configuration(metric_name, body, async_req=True)
        >>> result = thread.get()

        :param metric_name: The name of the metric.
        :type metric_name: str
        :type body: MetricTagConfigurationCreateRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricTagConfigurationResponse
        """
        kwargs = self._create_tag_configuration_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        kwargs["body"] = body

        return self._create_tag_configuration_endpoint.call_with_http_info(**kwargs)

    def delete_bulk_tags_metrics_configuration(self, body, **kwargs):
        """Configure tags for multiple metrics.

        Delete all custom lists of queryable tag keys for a set of existing count, gauge, rate, and distribution metrics.
        Metrics are selected by passing a metric name prefix.
        Results can be sent to a set of account email addresses, just like the same operation in the Datadog web app.
        Can only be used with application keys of users with the `Manage Tags for Metrics` permission.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_bulk_tags_metrics_configuration(body, async_req=True)
        >>> result = thread.get()

        :type body: MetricBulkTagConfigDeleteRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricBulkTagConfigResponse
        """
        kwargs = self._delete_bulk_tags_metrics_configuration_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._delete_bulk_tags_metrics_configuration_endpoint.call_with_http_info(**kwargs)

    def delete_tag_configuration(self, metric_name, **kwargs):
        """Delete a tag configuration.

        Deletes a metric's tag configuration. Can only be used with application
        keys from users with the `Manage Tags for Metrics` permission.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_tag_configuration(metric_name, async_req=True)
        >>> result = thread.get()

        :param metric_name: The name of the metric.
        :type metric_name: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: None
        """
        kwargs = self._delete_tag_configuration_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        return self._delete_tag_configuration_endpoint.call_with_http_info(**kwargs)

    def list_tag_configuration_by_name(self, metric_name, **kwargs):
        """List tag configuration by name.

        Returns the tag configuration for the given metric name.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_tag_configuration_by_name(metric_name, async_req=True)
        >>> result = thread.get()

        :param metric_name: The name of the metric.
        :type metric_name: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricTagConfigurationResponse
        """
        kwargs = self._list_tag_configuration_by_name_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        return self._list_tag_configuration_by_name_endpoint.call_with_http_info(**kwargs)

    def list_tag_configurations(self, **kwargs):
        """List tag configurations.

        Returns all configured count/gauge/rate/distribution metric names
        (with additional filters if specified).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_tag_configurations(async_req=True)
        >>> result = thread.get()

        :param filter_configured: Filter metrics that have configured tags.
        :type filter_configured: bool, optional
        :param filter_tags_configured: Filter tag configurations by configured tags.
        :type filter_tags_configured: str, optional
        :param filter_metric_type: Filter tag configurations by metric type.
        :type filter_metric_type: MetricTagConfigurationMetricTypes, optional
        :param filter_include_percentiles: Filter distributions with additional percentile
            aggregations enabled or disabled.
        :type filter_include_percentiles: bool, optional
        :param filter_tags: Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions.
            Cannot be combined with other filters.
        :type filter_tags: str, optional
        :param window_seconds: The number of seconds of look back (from now) to apply to a filter[tag] query.
            Defaults value is 3600 (1 hour), maximum value is 172,800 (2 days).
        :type window_seconds: int, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricsAndMetricTagConfigurationsResponse
        """
        kwargs = self._list_tag_configurations_endpoint.default_arguments(kwargs)
        return self._list_tag_configurations_endpoint.call_with_http_info(**kwargs)

    def list_tags_by_metric_name(self, metric_name, **kwargs):
        """List tags by metric name.

        View indexed tag key-value pairs for a given metric name.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_tags_by_metric_name(metric_name, async_req=True)
        >>> result = thread.get()

        :param metric_name: The name of the metric.
        :type metric_name: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricAllTagsResponse
        """
        kwargs = self._list_tags_by_metric_name_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        return self._list_tags_by_metric_name_endpoint.call_with_http_info(**kwargs)

    def list_volumes_by_metric_name(self, metric_name, **kwargs):
        """List distinct metric volumes by metric name.

        View distinct metrics volumes for the given metric name.

        Custom distribution metrics will return both ingested and indexed custom metric volumes.
        For Metrics without Limits&trade; beta customers, all metrics will return both ingested/indexed volumes.
        Custom metrics generated in-app from other products will return `null` for ingested volumes.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_volumes_by_metric_name(metric_name, async_req=True)
        >>> result = thread.get()

        :param metric_name: The name of the metric.
        :type metric_name: str
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricVolumesResponse
        """
        kwargs = self._list_volumes_by_metric_name_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        return self._list_volumes_by_metric_name_endpoint.call_with_http_info(**kwargs)

    def update_tag_configuration(self, metric_name, body, **kwargs):
        """Update a tag configuration.

        Update the tag configuration of a metric or percentile aggregations of a distribution metric or custom aggregations
        of a count, rate, or gauge metric.
        Can only be used with application keys from users with the `Manage Tags for Metrics` permission.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_tag_configuration(metric_name, body, async_req=True)
        >>> result = thread.get()

        :param metric_name: The name of the metric.
        :type metric_name: str
        :type body: MetricTagConfigurationUpdateRequest
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: MetricTagConfigurationResponse
        """
        kwargs = self._update_tag_configuration_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        kwargs["body"] = body

        return self._update_tag_configuration_endpoint.call_with_http_info(**kwargs)
