# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.metrics_list_response import MetricsListResponse
from datadog_api_client.v1.model.metric_metadata import MetricMetadata
from datadog_api_client.v1.model.metrics_query_response import MetricsQueryResponse
from datadog_api_client.v1.model.metric_search_response import MetricSearchResponse
from datadog_api_client.v1.model.intake_payload_accepted import IntakePayloadAccepted
from datadog_api_client.v1.model.metric_content_encoding import MetricContentEncoding
from datadog_api_client.v1.model.metrics_payload import MetricsPayload


class MetricsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._get_metric_metadata_endpoint = _Endpoint(
            settings={
                "response_type": (MetricMetadata,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/metrics/{metric_name}",
                "operation_id": "get_metric_metadata",
                "http_method": "GET",
                "version": "v1",
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

        self._list_active_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (MetricsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/metrics",
                "operation_id": "list_active_metrics",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "_from": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "from",
                    "location": "query",
                },
                "host": {
                    "openapi_types": (str,),
                    "attribute": "host",
                    "location": "query",
                },
                "tag_filter": {
                    "openapi_types": (str,),
                    "attribute": "tag_filter",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (MetricSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/search",
                "operation_id": "list_metrics",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "q": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "q",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._query_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (MetricsQueryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/query",
                "operation_id": "query_metrics",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "_from": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "to",
                    "location": "query",
                },
                "query": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._submit_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (IntakePayloadAccepted,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v1/series",
                "operation_id": "submit_metrics",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "content_encoding": {
                    "openapi_types": (MetricContentEncoding,),
                    "attribute": "Content-Encoding",
                    "location": "header",
                },
                "body": {
                    "required": True,
                    "openapi_types": (MetricsPayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["text/json", "application/json"], "content_type": ["text/json"]},
            api_client=api_client,
        )

        self._update_metric_metadata_endpoint = _Endpoint(
            settings={
                "response_type": (MetricMetadata,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/metrics/{metric_name}",
                "operation_id": "update_metric_metadata",
                "http_method": "PUT",
                "version": "v1",
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
                    "openapi_types": (MetricMetadata,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def get_metric_metadata(self, metric_name, **kwargs):
        """Get metric metadata.

        Get metadata about a specific metric.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_metric_metadata(metric_name, async_req=True)
        >>> result = thread.get()

        :param metric_name: Name of the metric for which to get metadata.
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
        :rtype: MetricMetadata
        """
        kwargs = self._get_metric_metadata_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        return self._get_metric_metadata_endpoint.call_with_http_info(**kwargs)

    def list_active_metrics(self, _from, **kwargs):
        """Get active metrics list.

        Get the list of actively reporting metrics from a given time until now.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_active_metrics(_from, async_req=True)
        >>> result = thread.get()

        :param _from: Seconds since the Unix epoch.
        :type _from: int
        :param host: Hostname for filtering the list of metrics returned.
            If set, metrics retrieved are those with the corresponding hostname tag.
        :type host: str, optional
        :param tag_filter: Filter metrics that have been submitted with the given tags. Supports boolean and wildcard expressions.
            Cannot be combined with other filters.
        :type tag_filter: str, optional
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
        :rtype: MetricsListResponse
        """
        kwargs = self._list_active_metrics_endpoint.default_arguments(kwargs)
        kwargs["_from"] = _from

        return self._list_active_metrics_endpoint.call_with_http_info(**kwargs)

    def list_metrics(self, q, **kwargs):
        """Search metrics.

        Search for metrics from the last 24 hours in Datadog.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_metrics(q, async_req=True)
        >>> result = thread.get()

        :param q: Query string to search metrics upon. Can optionally be prefixed with `metrics:`.
        :type q: str
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
        :rtype: MetricSearchResponse
        """
        kwargs = self._list_metrics_endpoint.default_arguments(kwargs)
        kwargs["q"] = q

        return self._list_metrics_endpoint.call_with_http_info(**kwargs)

    def query_metrics(self, _from, to, query, **kwargs):
        """Query timeseries points.

        Query timeseries points.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.query_metrics(_from, to, query, async_req=True)
        >>> result = thread.get()

        :param _from: Start of the queried time period, seconds since the Unix epoch.
        :type _from: int
        :param to: End of the queried time period, seconds since the Unix epoch.
        :type to: int
        :param query: Query string.
        :type query: str
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
        :rtype: MetricsQueryResponse
        """
        kwargs = self._query_metrics_endpoint.default_arguments(kwargs)
        kwargs["_from"] = _from

        kwargs["to"] = to

        kwargs["query"] = query

        return self._query_metrics_endpoint.call_with_http_info(**kwargs)

    def submit_metrics(self, body, **kwargs):
        """Submit metrics.

        The metrics end-point allows you to post time-series data that can be graphed on Datadog’s dashboards.
        The maximum payload size is 3.2 megabytes (3200000 bytes). Compressed payloads must have a decompressed size of less than 62 megabytes (62914560 bytes).

        If you’re submitting metrics directly to the Datadog API without using DogStatsD, expect:

        - 64 bits for the timestamp
        - 32 bits for the value
        - 40 bytes for the metric names
        - 50 bytes for the timeseries
        - The full payload is approximately 100 bytes. However, with the DogStatsD API,
        compression is applied, which reduces the payload size.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.submit_metrics(body, async_req=True)
        >>> result = thread.get()

        :type body: MetricsPayload
        :param content_encoding: HTTP header used to compress the media-type.
        :type content_encoding: MetricContentEncoding, optional
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
        :rtype: IntakePayloadAccepted
        """
        kwargs = self._submit_metrics_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._submit_metrics_endpoint.call_with_http_info(**kwargs)

    def update_metric_metadata(self, metric_name, body, **kwargs):
        """Edit metric metadata.

        Edit metadata of a specific metric. Find out more about [supported types](https://docs.datadoghq.com/developers/metrics).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_metric_metadata(metric_name, body, async_req=True)
        >>> result = thread.get()

        :param metric_name: Name of the metric for which to edit metadata.
        :type metric_name: str
        :param body: New metadata.
        :type body: MetricMetadata
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
        :rtype: MetricMetadata
        """
        kwargs = self._update_metric_metadata_endpoint.default_arguments(kwargs)
        kwargs["metric_name"] = metric_name

        kwargs["body"] = body

        return self._update_metric_metadata_endpoint.call_with_http_info(**kwargs)
