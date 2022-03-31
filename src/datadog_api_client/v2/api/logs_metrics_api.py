# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model.logs_metrics_response import LogsMetricsResponse
from datadog_api_client.v2.model.logs_metric_response import LogsMetricResponse
from datadog_api_client.v2.model.logs_metric_create_request import LogsMetricCreateRequest
from datadog_api_client.v2.model.logs_metric_update_request import LogsMetricUpdateRequest


class LogsMetricsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_logs_metric_endpoint = _Endpoint(
            settings={
                "response_type": (LogsMetricResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/metrics",
                "operation_id": "create_logs_metric",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsMetricCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_logs_metric_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/metrics/{metric_id}",
                "operation_id": "delete_logs_metric",
                "http_method": "DELETE",
                "version": "v2",
                "servers": None,
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
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_logs_metric_endpoint = _Endpoint(
            settings={
                "response_type": (LogsMetricResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/metrics/{metric_id}",
                "operation_id": "get_logs_metric",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
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
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_logs_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (LogsMetricsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/logs/config/metrics",
                "operation_id": "list_logs_metrics",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_logs_metric_endpoint = _Endpoint(
            settings={
                "response_type": (LogsMetricResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/config/metrics/{metric_id}",
                "operation_id": "update_logs_metric",
                "http_method": "PATCH",
                "version": "v2",
                "servers": None,
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
                    "openapi_types": (LogsMetricUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_logs_metric(self, body, **kwargs):
        """Create a log-based metric.

        Create a metric based on your ingested logs in your organization.
        Returns the log-based metric object from the request body when the request is successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_logs_metric(body, async_req=True)
        >>> result = thread.get()

        :param body: The definition of the new log-based metric.
        :type body: LogsMetricCreateRequest
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
        :rtype: LogsMetricResponse
        """
        kwargs = self._create_logs_metric_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_logs_metric_endpoint.call_with_http_info(**kwargs)

    def delete_logs_metric(self, metric_id, **kwargs):
        """Delete a log-based metric.

        Delete a specific log-based metric from your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_logs_metric(metric_id, async_req=True)
        >>> result = thread.get()

        :param metric_id: The name of the log-based metric.
        :type metric_id: str
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
        kwargs = self._delete_logs_metric_endpoint.default_arguments(kwargs)
        kwargs["metric_id"] = metric_id

        return self._delete_logs_metric_endpoint.call_with_http_info(**kwargs)

    def get_logs_metric(self, metric_id, **kwargs):
        """Get a log-based metric.

        Get a specific log-based metric from your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_logs_metric(metric_id, async_req=True)
        >>> result = thread.get()

        :param metric_id: The name of the log-based metric.
        :type metric_id: str
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
        :rtype: LogsMetricResponse
        """
        kwargs = self._get_logs_metric_endpoint.default_arguments(kwargs)
        kwargs["metric_id"] = metric_id

        return self._get_logs_metric_endpoint.call_with_http_info(**kwargs)

    def list_logs_metrics(self, **kwargs):
        """Get all log-based metrics.

        Get the list of configured log-based metrics with their definitions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_logs_metrics(async_req=True)
        >>> result = thread.get()

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
        :rtype: LogsMetricsResponse
        """
        kwargs = self._list_logs_metrics_endpoint.default_arguments(kwargs)
        return self._list_logs_metrics_endpoint.call_with_http_info(**kwargs)

    def update_logs_metric(self, metric_id, body, **kwargs):
        """Update a log-based metric.

        Update a specific log-based metric from your organization.
        Returns the log-based metric object from the request body when the request is successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_logs_metric(metric_id, body, async_req=True)
        >>> result = thread.get()

        :param metric_id: The name of the log-based metric.
        :type metric_id: str
        :param body: New definition of the log-based metric.
        :type body: LogsMetricUpdateRequest
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
        :rtype: LogsMetricResponse
        """
        kwargs = self._update_logs_metric_endpoint.default_arguments(kwargs)
        kwargs["metric_id"] = metric_id

        kwargs["body"] = body

        return self._update_logs_metric_endpoint.call_with_http_info(**kwargs)
