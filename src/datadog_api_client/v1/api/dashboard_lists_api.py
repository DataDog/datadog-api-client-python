# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.dashboard_list_list_response import DashboardListListResponse
from datadog_api_client.v1.model.dashboard_list import DashboardList
from datadog_api_client.v1.model.dashboard_list_delete_response import DashboardListDeleteResponse


class DashboardListsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_dashboard_list_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardList,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/lists/manual",
                "operation_id": "create_dashboard_list",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DashboardList,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_dashboard_list_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardListDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/lists/manual/{list_id}",
                "operation_id": "delete_dashboard_list",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "list_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "list_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_dashboard_list_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardList,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/lists/manual/{list_id}",
                "operation_id": "get_dashboard_list",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "list_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "list_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_dashboard_lists_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardListListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/lists/manual",
                "operation_id": "list_dashboard_lists",
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

        self._update_dashboard_list_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardList,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/lists/manual/{list_id}",
                "operation_id": "update_dashboard_list",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "list_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "list_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DashboardList,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_dashboard_list(self, body, **kwargs):
        """Create a dashboard list.

        Create an empty dashboard list.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_dashboard_list(body, async_req=True)
        >>> result = thread.get()

        :param body: Create a dashboard list request body.
        :type body: DashboardList
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
        :rtype: DashboardList
        """
        kwargs = self._create_dashboard_list_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_dashboard_list_endpoint.call_with_http_info(**kwargs)

    def delete_dashboard_list(self, list_id, **kwargs):
        """Delete a dashboard list.

        Delete a dashboard list.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_dashboard_list(list_id, async_req=True)
        >>> result = thread.get()

        :param list_id: ID of the dashboard list to delete.
        :type list_id: int
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
        :rtype: DashboardListDeleteResponse
        """
        kwargs = self._delete_dashboard_list_endpoint.default_arguments(kwargs)
        kwargs["list_id"] = list_id

        return self._delete_dashboard_list_endpoint.call_with_http_info(**kwargs)

    def get_dashboard_list(self, list_id, **kwargs):
        """Get a dashboard list.

        Fetch an existing dashboard list's definition.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_dashboard_list(list_id, async_req=True)
        >>> result = thread.get()

        :param list_id: ID of the dashboard list to fetch.
        :type list_id: int
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
        :rtype: DashboardList
        """
        kwargs = self._get_dashboard_list_endpoint.default_arguments(kwargs)
        kwargs["list_id"] = list_id

        return self._get_dashboard_list_endpoint.call_with_http_info(**kwargs)

    def list_dashboard_lists(self, **kwargs):
        """Get all dashboard lists.

        Fetch all of your existing dashboard list definitions.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_dashboard_lists(async_req=True)
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
        :rtype: DashboardListListResponse
        """
        kwargs = self._list_dashboard_lists_endpoint.default_arguments(kwargs)
        return self._list_dashboard_lists_endpoint.call_with_http_info(**kwargs)

    def update_dashboard_list(self, list_id, body, **kwargs):
        """Update a dashboard list.

        Update the name of a dashboard list.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_dashboard_list(list_id, body, async_req=True)
        >>> result = thread.get()

        :param list_id: ID of the dashboard list to update.
        :type list_id: int
        :param body: Update a dashboard list request body.
        :type body: DashboardList
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
        :rtype: DashboardList
        """
        kwargs = self._update_dashboard_list_endpoint.default_arguments(kwargs)
        kwargs["list_id"] = list_id

        kwargs["body"] = body

        return self._update_dashboard_list_endpoint.call_with_http_info(**kwargs)
