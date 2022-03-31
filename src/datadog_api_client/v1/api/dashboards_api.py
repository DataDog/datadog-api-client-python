# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.dashboard_bulk_delete_request import DashboardBulkDeleteRequest
from datadog_api_client.v1.model.dashboard_summary import DashboardSummary
from datadog_api_client.v1.model.dashboard_restore_request import DashboardRestoreRequest
from datadog_api_client.v1.model.dashboard import Dashboard
from datadog_api_client.v1.model.dashboard_delete_response import DashboardDeleteResponse


class DashboardsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (Dashboard,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "create_dashboard",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (Dashboard,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardDeleteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/{dashboard_id}",
                "operation_id": "delete_dashboard",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_dashboards_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "delete_dashboards",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DashboardBulkDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (Dashboard,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/{dashboard_id}",
                "operation_id": "get_dashboard",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_dashboards_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardSummary,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "list_dashboards",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "filter_shared": {
                    "openapi_types": (bool,),
                    "attribute": "filter[shared]",
                    "location": "query",
                },
                "filter_deleted": {
                    "openapi_types": (bool,),
                    "attribute": "filter[deleted]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._restore_dashboards_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard",
                "operation_id": "restore_dashboards",
                "http_method": "PATCH",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DashboardRestoreRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_dashboard_endpoint = _Endpoint(
            settings={
                "response_type": (Dashboard,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/dashboard/{dashboard_id}",
                "operation_id": "update_dashboard",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "dashboard_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "dashboard_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (Dashboard,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_dashboard(self, body, **kwargs):
        """Create a new dashboard.

        Create a dashboard using the specified options. When defining queries in your widgets, take note of which queries should have the `as_count()` or `as_rate()` modifiers appended.
        Refer to the following [documentation](https://docs.datadoghq.com/developers/metrics/type_modifiers/?tab=count#in-application-modifiers) for more information on these modifiers.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_dashboard(body, async_req=True)
        >>> result = thread.get()

        :param body: Create a dashboard request body.
        :type body: Dashboard
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
        :rtype: Dashboard
        """
        kwargs = self._create_dashboard_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_dashboard_endpoint.call_with_http_info(**kwargs)

    def delete_dashboard(self, dashboard_id, **kwargs):
        """Delete a dashboard.

        Delete a dashboard using the specified ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_dashboard(dashboard_id, async_req=True)
        >>> result = thread.get()

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
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
        :rtype: DashboardDeleteResponse
        """
        kwargs = self._delete_dashboard_endpoint.default_arguments(kwargs)
        kwargs["dashboard_id"] = dashboard_id

        return self._delete_dashboard_endpoint.call_with_http_info(**kwargs)

    def delete_dashboards(self, body, **kwargs):
        """Delete dashboards.

        Delete dashboards using the specified IDs. If there are any failures, no dashboards will be deleted (partial success is not allowed).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.delete_dashboards(body, async_req=True)
        >>> result = thread.get()

        :param body: Delete dashboards request body.
        :type body: DashboardBulkDeleteRequest
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
        kwargs = self._delete_dashboards_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._delete_dashboards_endpoint.call_with_http_info(**kwargs)

    def get_dashboard(self, dashboard_id, **kwargs):
        """Get a dashboard.

        Get a dashboard using the specified ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_dashboard(dashboard_id, async_req=True)
        >>> result = thread.get()

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
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
        :rtype: Dashboard
        """
        kwargs = self._get_dashboard_endpoint.default_arguments(kwargs)
        kwargs["dashboard_id"] = dashboard_id

        return self._get_dashboard_endpoint.call_with_http_info(**kwargs)

    def list_dashboards(self, **kwargs):
        """Get all dashboards.

        Get all dashboards.

        **Note**: This query will only return custom created or cloned dashboards.
        This query will not return preset dashboards.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_dashboards(async_req=True)
        >>> result = thread.get()

        :param filter_shared: When `true`, this query only returns shared custom created
            or cloned dashboards.
        :type filter_shared: bool, optional
        :param filter_deleted: When `true`, this query returns only deleted custom-created
            or cloned dashboards. This parameter is incompatible with `filter[shared]`.
        :type filter_deleted: bool, optional
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
        :rtype: DashboardSummary
        """
        kwargs = self._list_dashboards_endpoint.default_arguments(kwargs)
        return self._list_dashboards_endpoint.call_with_http_info(**kwargs)

    def restore_dashboards(self, body, **kwargs):
        """Restore deleted dashboards.

        Restore dashboards using the specified IDs. If there are any failures, no dashboards will be restored (partial success is not allowed).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.restore_dashboards(body, async_req=True)
        >>> result = thread.get()

        :param body: Restore dashboards request body.
        :type body: DashboardRestoreRequest
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
        kwargs = self._restore_dashboards_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._restore_dashboards_endpoint.call_with_http_info(**kwargs)

    def update_dashboard(self, dashboard_id, body, **kwargs):
        """Update a dashboard.

        Update a dashboard using the specified ID.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.update_dashboard(dashboard_id, body, async_req=True)
        >>> result = thread.get()

        :param dashboard_id: The ID of the dashboard.
        :type dashboard_id: str
        :param body: Update Dashboard request body.
        :type body: Dashboard
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
        :rtype: Dashboard
        """
        kwargs = self._update_dashboard_endpoint.default_arguments(kwargs)
        kwargs["dashboard_id"] = dashboard_id

        kwargs["body"] = body

        return self._update_dashboard_endpoint.call_with_http_info(**kwargs)
