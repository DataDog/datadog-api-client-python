# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.logs_indexes_order import LogsIndexesOrder
from datadog_api_client.v1.model.logs_index_list_response import LogsIndexListResponse
from datadog_api_client.v1.model.logs_index import LogsIndex
from datadog_api_client.v1.model.logs_index_update_request import LogsIndexUpdateRequest


class LogsIndexesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_logs_index_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndex,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/indexes",
                "operation_id": "create_logs_index",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsIndex,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_logs_index_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndex,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/indexes/{name}",
                "operation_id": "get_logs_index",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_logs_index_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndexesOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/logs/config/index-order",
                "operation_id": "get_logs_index_order",
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

        self._list_log_indexes_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndexListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/logs/config/indexes",
                "operation_id": "list_log_indexes",
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

        self._update_logs_index_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndex,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/indexes/{name}",
                "operation_id": "update_logs_index",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (LogsIndexUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_logs_index_order_endpoint = _Endpoint(
            settings={
                "response_type": (LogsIndexesOrder,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/logs/config/index-order",
                "operation_id": "update_logs_index_order",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (LogsIndexesOrder,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_logs_index(self, body, **kwargs):
        """Create an index.

        Creates a new index. Returns the Index object passed in the request body when the request is successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_logs_index(body, async_req=True)
        >>> result = thread.get()

        :param body: Object containing the new index.
        :type body: LogsIndex
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
        :rtype: LogsIndex
        """
        kwargs = self._create_logs_index_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_logs_index_endpoint.call_with_http_info(**kwargs)

    def get_logs_index(self, name, **kwargs):
        """Get an index.

        Get one log index from your organization. This endpoint takes no JSON arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_logs_index(name, async_req=True)
        >>> result = thread.get()

        :param name: Name of the log index.
        :type name: str
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
        :rtype: LogsIndex
        """
        kwargs = self._get_logs_index_endpoint.default_arguments(kwargs)
        kwargs["name"] = name

        return self._get_logs_index_endpoint.call_with_http_info(**kwargs)

    def get_logs_index_order(self, **kwargs):
        """Get indexes order.

        Get the current order of your log indexes. This endpoint takes no JSON arguments.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_logs_index_order(async_req=True)
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
        :rtype: LogsIndexesOrder
        """
        kwargs = self._get_logs_index_order_endpoint.default_arguments(kwargs)
        return self._get_logs_index_order_endpoint.call_with_http_info(**kwargs)

    def list_log_indexes(self, **kwargs):
        """Get all indexes.

        The Index object describes the configuration of a log index.
        This endpoint returns an array of the `LogIndex` objects of your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_log_indexes(async_req=True)
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
        :rtype: LogsIndexListResponse
        """
        kwargs = self._list_log_indexes_endpoint.default_arguments(kwargs)
        return self._list_log_indexes_endpoint.call_with_http_info(**kwargs)

    def update_logs_index(self, name, body, **kwargs):
        """Update an index.

        Update an index as identified by its name.
        Returns the Index object passed in the request body when the request is successful.

        Using the `PUT` method updates your index’s configuration by **replacing**
        your current configuration with the new one sent to your Datadog organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_logs_index(name, body, async_req=True)
        >>> result = thread.get()

        :param name: Name of the log index.
        :type name: str
        :param body: Object containing the new `LogsIndexUpdateRequest`.
        :type body: LogsIndexUpdateRequest
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
        :rtype: LogsIndex
        """
        kwargs = self._update_logs_index_endpoint.default_arguments(kwargs)
        kwargs["name"] = name

        kwargs["body"] = body

        return self._update_logs_index_endpoint.call_with_http_info(**kwargs)

    def update_logs_index_order(self, body, **kwargs):
        """Update indexes order.

        This endpoint updates the index order of your organization.
        It returns the index order object passed in the request body when the request is successful.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_logs_index_order(body, async_req=True)
        >>> result = thread.get()

        :param body: Object containing the new ordered list of index names
        :type body: LogsIndexesOrder
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
        :rtype: LogsIndexesOrder
        """
        kwargs = self._update_logs_index_order_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._update_logs_index_order_endpoint.call_with_http_info(**kwargs)
