# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.logs_pipelines_order import LogsPipelinesOrder
from datadog_api_client.v1.model.logs_pipeline_list import LogsPipelineList
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline


class LogsPipelinesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_logs_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (LogsPipeline,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/pipelines",
                "operation_id": "create_logs_pipeline",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsPipeline,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_logs_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/pipelines/{pipeline_id}",
                "operation_id": "delete_logs_pipeline",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "pipeline_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "pipeline_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_logs_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (LogsPipeline,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/logs/config/pipelines/{pipeline_id}",
                "operation_id": "get_logs_pipeline",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "pipeline_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "pipeline_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_logs_pipeline_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsPipelinesOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/logs/config/pipeline-order",
                "operation_id": "get_logs_pipeline_order",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_logs_pipelines_endpoint = _Endpoint(
            settings={
                "response_type": (LogsPipelineList,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/logs/config/pipelines",
                "operation_id": "list_logs_pipelines",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_logs_pipeline_endpoint = _Endpoint(
            settings={
                "response_type": (LogsPipeline,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/pipelines/{pipeline_id}",
                "operation_id": "update_logs_pipeline",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "pipeline_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "pipeline_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LogsPipeline,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_logs_pipeline_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsPipelinesOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/pipeline-order",
                "operation_id": "update_logs_pipeline_order",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsPipelinesOrder,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_logs_pipeline(self, body, **kwargs):
        """Create a pipeline.

        Create a pipeline in your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_logs_pipeline(body, async_req=True)
        >>> result = thread.get()

        :param body: Definition of the new pipeline.
        :type body: LogsPipeline
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
        :rtype: LogsPipeline
        """
        kwargs = self._create_logs_pipeline_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_logs_pipeline_endpoint.call_with_http_info(**kwargs)

    def delete_logs_pipeline(self, pipeline_id, **kwargs):
        """Delete a pipeline.

        Delete a given pipeline from your organization.
        This endpoint takes no JSON arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_logs_pipeline(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: ID of the pipeline to delete.
        :type pipeline_id: str
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
        kwargs = self._delete_logs_pipeline_endpoint.default_arguments(kwargs)
        kwargs["pipeline_id"] = pipeline_id

        return self._delete_logs_pipeline_endpoint.call_with_http_info(**kwargs)

    def get_logs_pipeline(self, pipeline_id, **kwargs):
        """Get a pipeline.

        Get a specific pipeline from your organization.
        This endpoint takes no JSON arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_logs_pipeline(pipeline_id, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: ID of the pipeline to get.
        :type pipeline_id: str
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
        :rtype: LogsPipeline
        """
        kwargs = self._get_logs_pipeline_endpoint.default_arguments(kwargs)
        kwargs["pipeline_id"] = pipeline_id

        return self._get_logs_pipeline_endpoint.call_with_http_info(**kwargs)

    def get_logs_pipeline_order(self, **kwargs):
        """Get pipeline order.

        Get the current order of your pipelines.
        This endpoint takes no JSON arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_logs_pipeline_order(async_req=True)
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
        :rtype: LogsPipelinesOrder
        """
        kwargs = self._get_logs_pipeline_order_endpoint.default_arguments(kwargs)
        return self._get_logs_pipeline_order_endpoint.call_with_http_info(**kwargs)

    def list_logs_pipelines(self, **kwargs):
        """Get all pipelines.

        Get all pipelines from your organization.
        This endpoint takes no JSON arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_logs_pipelines(async_req=True)
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
        :rtype: LogsPipelineList
        """
        kwargs = self._list_logs_pipelines_endpoint.default_arguments(kwargs)
        return self._list_logs_pipelines_endpoint.call_with_http_info(**kwargs)

    def update_logs_pipeline(self, pipeline_id, body, **kwargs):
        """Update a pipeline.

        Update a given pipeline configuration to change it’s processors or their order.

        **Note**: Using this method updates your pipeline configuration by **replacing**
        your current configuration with the new one sent to your Datadog organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_logs_pipeline(pipeline_id, body, async_req=True)
        >>> result = thread.get()

        :param pipeline_id: ID of the pipeline to delete.
        :type pipeline_id: str
        :param body: New definition of the pipeline.
        :type body: LogsPipeline
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
        :rtype: LogsPipeline
        """
        kwargs = self._update_logs_pipeline_endpoint.default_arguments(kwargs)
        kwargs["pipeline_id"] = pipeline_id

        kwargs["body"] = body

        return self._update_logs_pipeline_endpoint.call_with_http_info(**kwargs)

    def update_logs_pipeline_order(self, body, **kwargs):
        """Update pipeline order.

        Update the order of your pipelines. Since logs are processed sequentially, reordering a pipeline may change
        the structure and content of the data processed by other pipelines and their processors.

        **Note**: Using the `PUT` method updates your pipeline order by replacing your current order
        with the new one sent to your Datadog organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_logs_pipeline_order(body, async_req=True)
        >>> result = thread.get()

        :param body: Object containing the new ordered list of pipeline IDs.
        :type body: LogsPipelinesOrder
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
        :rtype: LogsPipelinesOrder
        """
        kwargs = self._update_logs_pipeline_order_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._update_logs_pipeline_order_endpoint.call_with_http_info(**kwargs)
