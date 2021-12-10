# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    date,
    datetime,
    file_type,
    none_type,
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.security_filter_create_request import SecurityFilterCreateRequest
from datadog_api_client.v2.model.security_filter_response import SecurityFilterResponse
from datadog_api_client.v2.model.security_filter_update_request import SecurityFilterUpdateRequest
from datadog_api_client.v2.model.security_filters_response import SecurityFiltersResponse
from datadog_api_client.v2.model.security_monitoring_list_rules_response import SecurityMonitoringListRulesResponse
from datadog_api_client.v2.model.security_monitoring_rule_create_payload import SecurityMonitoringRuleCreatePayload
from datadog_api_client.v2.model.security_monitoring_rule_response import SecurityMonitoringRuleResponse
from datadog_api_client.v2.model.security_monitoring_rule_update_payload import SecurityMonitoringRuleUpdatePayload
from datadog_api_client.v2.model.security_monitoring_signal_list_request import SecurityMonitoringSignalListRequest
from datadog_api_client.v2.model.security_monitoring_signals_list_response import SecurityMonitoringSignalsListResponse
from datadog_api_client.v2.model.security_monitoring_signals_sort import SecurityMonitoringSignalsSort


class SecurityMonitoringApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFilterResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters",
                "operation_id": "create_security_filter",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityFilterCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/rules",
                "operation_id": "create_security_monitoring_rule",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleCreatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters/{security_filter_id}",
                "operation_id": "delete_security_filter",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "security_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "security_filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._delete_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}",
                "operation_id": "delete_security_monitoring_rule",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFilterResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters/{security_filter_id}",
                "operation_id": "get_security_filter",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "security_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "security_filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}",
                "operation_id": "get_security_monitoring_rule",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_security_filters_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFiltersResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters",
                "operation_id": "list_security_filters",
                "http_method": "GET",
                "servers": None,
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_rules_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringListRulesResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/rules",
                "operation_id": "list_security_monitoring_rules",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_security_monitoring_signals_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsListResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/signals",
                "operation_id": "list_security_monitoring_signals",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (SecurityMonitoringSignalsSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._search_security_monitoring_signals_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringSignalsListResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/signals/search",
                "operation_id": "search_security_monitoring_signals",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "body": {
                    "openapi_types": (SecurityMonitoringSignalListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_filter_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityFilterResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/configuration/security_filters/{security_filter_id}",
                "operation_id": "update_security_filter",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "security_filter_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "security_filter_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityFilterUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_security_monitoring_rule_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityMonitoringRuleResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/security_monitoring/rules/{rule_id}",
                "operation_id": "update_security_monitoring_rule",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SecurityMonitoringRuleUpdatePayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_security_filter(self, body, **kwargs):
        """Create a security filter

        Create a security filter.  See the [security filter guide](https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/) for more examples.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_security_filter(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (SecurityFilterCreateRequest): The definition of the new security filter.

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
            SecurityFilterResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_security_filter_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_security_filter_endpoint.call_with_http_info(**kwargs)

    def create_security_monitoring_rule(self, body, **kwargs):
        """Create a detection rule

        Create a detection rule.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_security_monitoring_rule(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (SecurityMonitoringRuleCreatePayload):

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
            SecurityMonitoringRuleResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_security_monitoring_rule_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def delete_security_filter(self, security_filter_id, **kwargs):
        """Delete a security filter

        Delete a specific security filter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_security_filter(security_filter_id, async_req=True)
        >>> result = thread.get()

        Args:
            security_filter_id (str): The ID of the security filter.

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
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_security_filter_endpoint.default_arguments(kwargs)
        kwargs["security_filter_id"] = security_filter_id
        return self._delete_security_filter_endpoint.call_with_http_info(**kwargs)

    def delete_security_monitoring_rule(self, rule_id, **kwargs):
        """Delete an existing rule

        Delete an existing rule. Default rules cannot be deleted.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_security_monitoring_rule(rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            rule_id (str): The ID of the rule.

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
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._delete_security_monitoring_rule_endpoint.default_arguments(kwargs)
        kwargs["rule_id"] = rule_id
        return self._delete_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def get_security_filter(self, security_filter_id, **kwargs):
        """Get a security filter

        Get the details of a specific security filter.  See the [security filter guide](https://docs.datadoghq.com/security_platform/guide/how-to-setup-security-filters-using-security-monitoring-api/) for more examples.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_security_filter(security_filter_id, async_req=True)
        >>> result = thread.get()

        Args:
            security_filter_id (str): The ID of the security filter.

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
            SecurityFilterResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_security_filter_endpoint.default_arguments(kwargs)
        kwargs["security_filter_id"] = security_filter_id
        return self._get_security_filter_endpoint.call_with_http_info(**kwargs)

    def get_security_monitoring_rule(self, rule_id, **kwargs):
        """Get a rule's details

        Get a rule's details.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_security_monitoring_rule(rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            rule_id (str): The ID of the rule.

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
            SecurityMonitoringRuleResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_security_monitoring_rule_endpoint.default_arguments(kwargs)
        kwargs["rule_id"] = rule_id
        return self._get_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)

    def list_security_filters(self, **kwargs):
        """Get all security filters

        Get the list of configured security filters with their definitions.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_security_filters(async_req=True)
        >>> result = thread.get()


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
            SecurityFiltersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_security_filters_endpoint.default_arguments(kwargs)
        return self._list_security_filters_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_rules(self, **kwargs):
        """List rules

        List rules.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_security_monitoring_rules(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page_size (int): Size for a given page.. [optional] if omitted the server will use the default value of 10
            page_number (int): Specific page number to return.. [optional] if omitted the server will use the default value of 0
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
            SecurityMonitoringListRulesResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_security_monitoring_rules_endpoint.default_arguments(kwargs)
        return self._list_security_monitoring_rules_endpoint.call_with_http_info(**kwargs)

    def list_security_monitoring_signals(self, **kwargs):
        """Get a quick list of security signals

        The list endpoint returns security signals that match a search query. Both this endpoint and the POST endpoint can be used interchangeably when listing security signals.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_security_monitoring_signals(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_query (str): The search query for security signals.. [optional]
            filter_from (datetime): The minimum timestamp for requested security signals.. [optional]
            filter_to (datetime): The maximum timestamp for requested security signals.. [optional]
            sort (SecurityMonitoringSignalsSort): The order of the security signals in results.. [optional]
            page_cursor (str): A list of results using the cursor provided in the previous query.. [optional]
            page_limit (int): The maximum number of security signals in the response.. [optional] if omitted the server will use the default value of 10
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
            SecurityMonitoringSignalsListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_security_monitoring_signals_endpoint.default_arguments(kwargs)
        return self._list_security_monitoring_signals_endpoint.call_with_http_info(**kwargs)

    def search_security_monitoring_signals(self, **kwargs):
        """Get a list of security signals

        Returns security signals that match a search query. Both this endpoint and the GET endpoint can be used interchangeably for listing security signals.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_security_monitoring_signals(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            body (SecurityMonitoringSignalListRequest): [optional]
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
            SecurityMonitoringSignalsListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._search_security_monitoring_signals_endpoint.default_arguments(kwargs)
        return self._search_security_monitoring_signals_endpoint.call_with_http_info(**kwargs)

    def update_security_filter(self, security_filter_id, body, **kwargs):
        """Update a security filter

        Update a specific security filter. Returns the security filter object when the request is successful.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_security_filter(security_filter_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            security_filter_id (str): The ID of the security filter.
            body (SecurityFilterUpdateRequest): New definition of the security filter.

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
            SecurityFilterResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_security_filter_endpoint.default_arguments(kwargs)
        kwargs["security_filter_id"] = security_filter_id
        kwargs["body"] = body
        return self._update_security_filter_endpoint.call_with_http_info(**kwargs)

    def update_security_monitoring_rule(self, rule_id, body, **kwargs):
        """Update an existing rule

        Update an existing rule. When updating `cases`, `queries` or `options`, the whole field must be included. For example, when modifying a query all queries must be included. Default rules can only be updated to be enabled and to change notifications.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_security_monitoring_rule(rule_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            rule_id (str): The ID of the rule.
            body (SecurityMonitoringRuleUpdatePayload):

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
            SecurityMonitoringRuleResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_security_monitoring_rule_endpoint.default_arguments(kwargs)
        kwargs["rule_id"] = rule_id
        kwargs["body"] = body
        return self._update_security_monitoring_rule_endpoint.call_with_http_info(**kwargs)
