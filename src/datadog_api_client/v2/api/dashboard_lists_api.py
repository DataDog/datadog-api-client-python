# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.dashboard_list_add_items_request import DashboardListAddItemsRequest
from datadog_api_client.v2.model.dashboard_list_add_items_response import DashboardListAddItemsResponse
from datadog_api_client.v2.model.dashboard_list_delete_items_request import DashboardListDeleteItemsRequest
from datadog_api_client.v2.model.dashboard_list_delete_items_response import DashboardListDeleteItemsResponse
from datadog_api_client.v2.model.dashboard_list_items import DashboardListItems
from datadog_api_client.v2.model.dashboard_list_update_items_request import DashboardListUpdateItemsRequest
from datadog_api_client.v2.model.dashboard_list_update_items_response import DashboardListUpdateItemsResponse


class DashboardListsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_dashboard_list_items_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardListAddItemsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards",
                "operation_id": "create_dashboard_list_items",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "dashboard_list_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "dashboard_list_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DashboardListAddItemsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_dashboard_list_items_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardListDeleteItemsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards",
                "operation_id": "delete_dashboard_list_items",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "dashboard_list_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "dashboard_list_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DashboardListDeleteItemsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_dashboard_list_items_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardListItems,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards",
                "operation_id": "get_dashboard_list_items",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "dashboard_list_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "dashboard_list_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_dashboard_list_items_endpoint = _Endpoint(
            settings={
                "response_type": (DashboardListUpdateItemsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dashboard/lists/manual/{dashboard_list_id}/dashboards",
                "operation_id": "update_dashboard_list_items",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "dashboard_list_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "dashboard_list_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DashboardListUpdateItemsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_dashboard_list_items(self, dashboard_list_id, body, **kwargs):
        """Add Items to a Dashboard List  # noqa: E501

        Add dashboards to an existing dashboard list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dashboard_list_items(dashboard_list_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            dashboard_list_id (int): ID of the dashboard list to add items to.
            body (DashboardListAddItemsRequest): Dashboards to add to the dashboard list.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DashboardListAddItemsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_dashboard_list_items_endpoint.default_arguments(kwargs)
        kwargs["dashboard_list_id"] = dashboard_list_id
        kwargs["body"] = body
        return self._create_dashboard_list_items_endpoint.call_with_http_info(**kwargs)

    def delete_dashboard_list_items(self, dashboard_list_id, body, **kwargs):
        """Delete items from a dashboard list  # noqa: E501

        Delete dashboards from an existing dashboard list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dashboard_list_items(dashboard_list_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            dashboard_list_id (int): ID of the dashboard list to delete items from.
            body (DashboardListDeleteItemsRequest): Dashboards to delete from the dashboard list.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DashboardListDeleteItemsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_dashboard_list_items_endpoint.default_arguments(kwargs)
        kwargs["dashboard_list_id"] = dashboard_list_id
        kwargs["body"] = body
        return self._delete_dashboard_list_items_endpoint.call_with_http_info(**kwargs)

    def get_dashboard_list_items(self, dashboard_list_id, **kwargs):
        """Get items of a Dashboard List  # noqa: E501

        Fetch the dashboard list’s dashboard definitions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dashboard_list_items(dashboard_list_id, async_req=True)
        >>> result = thread.get()

        Args:
            dashboard_list_id (int): ID of the dashboard list to get items from.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DashboardListItems
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_dashboard_list_items_endpoint.default_arguments(kwargs)
        kwargs["dashboard_list_id"] = dashboard_list_id
        return self._get_dashboard_list_items_endpoint.call_with_http_info(**kwargs)

    def update_dashboard_list_items(self, dashboard_list_id, body, **kwargs):
        """Update items of a dashboard list  # noqa: E501

        Update dashboards of an existing dashboard list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dashboard_list_items(dashboard_list_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            dashboard_list_id (int): ID of the dashboard list to update items from.
            body (DashboardListUpdateItemsRequest): New dashboards of the dashboard list.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DashboardListUpdateItemsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_dashboard_list_items_endpoint.default_arguments(kwargs)
        kwargs["dashboard_list_id"] = dashboard_list_id
        kwargs["body"] = body
        return self._update_dashboard_list_items_endpoint.call_with_http_info(**kwargs)
