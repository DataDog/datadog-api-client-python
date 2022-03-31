# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.downtime import Downtime
from datadog_api_client.v1.model.canceled_downtimes_ids import CanceledDowntimesIds
from datadog_api_client.v1.model.cancel_downtimes_by_scope_request import CancelDowntimesByScopeRequest


class DowntimesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._cancel_downtime_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime/{downtime_id}",
                "operation_id": "cancel_downtime",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._cancel_downtimes_by_scope_endpoint = _Endpoint(
            settings={
                "response_type": (CanceledDowntimesIds,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime/cancel/by_scope",
                "operation_id": "cancel_downtimes_by_scope",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CancelDowntimesByScopeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (Downtime,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime",
                "operation_id": "create_downtime",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Downtime,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (Downtime,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime/{downtime_id}",
                "operation_id": "get_downtime",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_downtimes_endpoint = _Endpoint(
            settings={
                "response_type": ([Downtime],),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime",
                "operation_id": "list_downtimes",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "current_only": {
                    "openapi_types": (bool,),
                    "attribute": "current_only",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_monitor_downtimes_endpoint = _Endpoint(
            settings={
                "response_type": ([Downtime],),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/monitor/{monitor_id}/downtimes",
                "operation_id": "list_monitor_downtimes",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "monitor_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "monitor_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (Downtime,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/downtime/{downtime_id}",
                "operation_id": "update_downtime",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Downtime,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def cancel_downtime(self, downtime_id, **kwargs):
        """Cancel a downtime.

        Cancel a downtime.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.cancel_downtime(downtime_id, async_req=True)
        >>> result = thread.get()

        :param downtime_id: ID of the downtime to cancel.
        :type downtime_id: int
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
        kwargs = self._cancel_downtime_endpoint.default_arguments(kwargs)
        kwargs["downtime_id"] = downtime_id

        return self._cancel_downtime_endpoint.call_with_http_info(**kwargs)

    def cancel_downtimes_by_scope(self, body, **kwargs):
        """Cancel downtimes by scope.

        Delete all downtimes that match the scope of `X`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.cancel_downtimes_by_scope(body, async_req=True)
        >>> result = thread.get()

        :param body: Scope to cancel downtimes for.
        :type body: CancelDowntimesByScopeRequest
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
        :rtype: CanceledDowntimesIds
        """
        kwargs = self._cancel_downtimes_by_scope_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._cancel_downtimes_by_scope_endpoint.call_with_http_info(**kwargs)

    def create_downtime(self, body, **kwargs):
        """Schedule a downtime.

        Schedule a downtime.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_downtime(body, async_req=True)
        >>> result = thread.get()

        :param body: Schedule a downtime request body.
        :type body: Downtime
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
        :rtype: Downtime
        """
        kwargs = self._create_downtime_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_downtime_endpoint.call_with_http_info(**kwargs)

    def get_downtime(self, downtime_id, **kwargs):
        """Get a downtime.

        Get downtime detail by `downtime_id`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_downtime(downtime_id, async_req=True)
        >>> result = thread.get()

        :param downtime_id: ID of the downtime to fetch.
        :type downtime_id: int
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
        :rtype: Downtime
        """
        kwargs = self._get_downtime_endpoint.default_arguments(kwargs)
        kwargs["downtime_id"] = downtime_id

        return self._get_downtime_endpoint.call_with_http_info(**kwargs)

    def list_downtimes(self, **kwargs):
        """Get all downtimes.

        Get all scheduled downtimes.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_downtimes(async_req=True)
        >>> result = thread.get()

        :param current_only: Only return downtimes that are active when the request is made.
        :type current_only: bool, optional
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
        :rtype: [Downtime]
        """
        kwargs = self._list_downtimes_endpoint.default_arguments(kwargs)
        return self._list_downtimes_endpoint.call_with_http_info(**kwargs)

    def list_monitor_downtimes(self, monitor_id, **kwargs):
        """Get all downtimes for a monitor.

        Get all active downtimes for the specified monitor.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_monitor_downtimes(monitor_id, async_req=True)
        >>> result = thread.get()

        :param monitor_id: The id of the monitor
        :type monitor_id: int
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
        :rtype: [Downtime]
        """
        kwargs = self._list_monitor_downtimes_endpoint.default_arguments(kwargs)
        kwargs["monitor_id"] = monitor_id

        return self._list_monitor_downtimes_endpoint.call_with_http_info(**kwargs)

    def update_downtime(self, downtime_id, body, **kwargs):
        """Update a downtime.

        Update a single downtime by `downtime_id`.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_downtime(downtime_id, body, async_req=True)
        >>> result = thread.get()

        :param downtime_id: ID of the downtime to update.
        :type downtime_id: int
        :param body: Update a downtime request body.
        :type body: Downtime
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
        :rtype: Downtime
        """
        kwargs = self._update_downtime_endpoint.default_arguments(kwargs)
        kwargs["downtime_id"] = downtime_id

        kwargs["body"] = body

        return self._update_downtime_endpoint.call_with_http_info(**kwargs)
