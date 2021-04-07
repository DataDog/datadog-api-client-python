# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest
from datadog_api_client.v2.model.logs_aggregate_response import LogsAggregateResponse
from datadog_api_client.v2.model.logs_list_request import LogsListRequest
from datadog_api_client.v2.model.logs_list_response import LogsListResponse
from datadog_api_client.v2.model.logs_sort import LogsSort


class LogsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._aggregate_logs_endpoint = _Endpoint(
            settings={
                "response_type": (LogsAggregateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/analytics/aggregate",
                "operation_id": "aggregate_logs",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (LogsAggregateRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_logs_endpoint = _Endpoint(
            settings={
                "response_type": (LogsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/events/search",
                "operation_id": "list_logs",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (LogsListRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_logs_get_endpoint = _Endpoint(
            settings={
                "response_type": (LogsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/logs/events",
                "operation_id": "list_logs_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "filter_query",
                    "filter_index",
                    "filter_from",
                    "filter_to",
                    "sort",
                    "page_cursor",
                    "page_limit",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [
                    "page_limit",
                ],
            },
            root_map={
                "validations": {
                    ("page_limit",): {
                        "inclusive_maximum": 1000,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "filter_query": (str,),
                    "filter_index": (str,),
                    "filter_from": (datetime,),
                    "filter_to": (datetime,),
                    "sort": (LogsSort,),
                    "page_cursor": (str,),
                    "page_limit": (int,),
                },
                "attribute_map": {
                    "filter_query": "filter[query]",
                    "filter_index": "filter[index]",
                    "filter_from": "filter[from]",
                    "filter_to": "filter[to]",
                    "sort": "sort",
                    "page_cursor": "page[cursor]",
                    "page_limit": "page[limit]",
                },
                "location_map": {
                    "filter_query": "query",
                    "filter_index": "query",
                    "filter_from": "query",
                    "filter_to": "query",
                    "sort": "query",
                    "page_cursor": "query",
                    "page_limit": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def aggregate_logs(self, body, **kwargs):
        """Aggregate events  # noqa: E501

        The API endpoint to aggregate events into buckets and compute metrics and timeseries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.aggregate_logs(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (LogsAggregateRequest):

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
            LogsAggregateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._aggregate_logs_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._aggregate_logs_endpoint.call_with_http_info(**kwargs)

    def list_logs(self, **kwargs):
        """Search logs  # noqa: E501

        List endpoint returns logs that match a log search query. [Results are paginated][1].  Use this endpoint to build complex logs filtering and search.  **If you are considering archiving logs for your organization, consider use of the Datadog archive capabilities instead of the log list API. See [Datadog Logs Archive documentation][2].**  [1]: /logs/guide/collect-multiple-logs-with-pagination [2]: https://docs.datadoghq.com/logs/archives  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_logs(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            body (LogsListRequest): [optional]
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
            LogsListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_logs_endpoint.default_arguments(kwargs)
        return self._list_logs_endpoint.call_with_http_info(**kwargs)

    def list_logs_get(self, **kwargs):
        """Get a list of logs  # noqa: E501

        List endpoint returns logs that match a log search query. [Results are paginated][1].  Use this endpoint to see your latest logs.  **If you are considering archiving logs for your organization, consider use of the Datadog archive capabilities instead of the log list API. See [Datadog Logs Archive documentation][2].**  [1]: /logs/guide/collect-multiple-logs-with-pagination [2]: https://docs.datadoghq.com/logs/archives  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_logs_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_query (str): Search query following logs syntax.. [optional]
            filter_index (str): For customers with multiple indexes, the indexes to search Defaults to '*' which means all indexes. [optional]
            filter_from (datetime): Minimum timestamp for requested logs.. [optional]
            filter_to (datetime): Maximum timestamp for requested logs.. [optional]
            sort (LogsSort): Order of logs in results.. [optional]
            page_cursor (str): List following results with a cursor provided in the previous query.. [optional]
            page_limit (int): Maximum number of logs in the response.. [optional] if omitted the server will use the default value of 10
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
            LogsListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_logs_get_endpoint.default_arguments(kwargs)
        return self._list_logs_get_endpoint.call_with_http_info(**kwargs)
