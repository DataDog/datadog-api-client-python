# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
)
from datadog_api_client.v2.model.process_summaries_response import ProcessSummariesResponse


class ProcessesApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._list_processes_endpoint = _Endpoint(
            settings={
                "response_type": (ProcessSummariesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/processes",
                "operation_id": "list_processes",
                "http_method": "GET",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": (str,),
                    "attribute": "tags",
                    "location": "query",
                },
                "_from": {
                    "openapi_types": (int,),
                    "attribute": "from",
                    "location": "query",
                },
                "to": {
                    "openapi_types": (int,),
                    "attribute": "to",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 10000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def list_processes(self, **kwargs):
        """Get all processes.

        Get all processes for your organization.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_processes(async_req=True)
        >>> result = thread.get()

        :param search: String to search processes by.
        :type search: str, optional
        :param tags: Comma-separated list of tags to filter processes by.
        :type tags: str, optional
        :param _from: Unix timestamp (number of seconds since epoch) of the start of the query window.
            If not provided, the start of the query window will be 15 minutes before the `to` timestamp. If neither
            `from` nor `to` are provided, the query window will be `[now - 15m, now]`.
        :type _from: int, optional
        :param to: Unix timestamp (number of seconds since epoch) of the end of the query window.
            If not provided, the end of the query window will be 15 minutes after the `from` timestamp. If neither
            `from` nor `to` are provided, the query window will be `[now - 15m, now]`.
        :type to: int, optional
        :param page_limit: Maximum number of results returned.
        :type page_limit: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in `meta.page.after`.
        :type page_cursor: str, optional
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
        :rtype: ProcessSummariesResponse
        """
        kwargs = self._list_processes_endpoint.default_arguments(kwargs)
        return self._list_processes_endpoint.call_with_http_info(**kwargs)

    def list_processes_with_pagination(self, **kwargs):
        """Get all processes.

        Provide a paginated version of :meth:`list_processes`, returning all items.

        :param search: String to search processes by.
        :type search: str, optional
        :param tags: Comma-separated list of tags to filter processes by.
        :type tags: str, optional
        :param _from: Unix timestamp (number of seconds since epoch) of the start of the query window.
            If not provided, the start of the query window will be 15 minutes before the `to` timestamp. If neither
            `from` nor `to` are provided, the query window will be `[now - 15m, now]`.
        :type _from: int, optional
        :param to: Unix timestamp (number of seconds since epoch) of the end of the query window.
            If not provided, the end of the query window will be 15 minutes after the `from` timestamp. If neither
            `from` nor `to` are provided, the query window will be `[now - 15m, now]`.
        :type to: int, optional
        :param page_limit: Maximum number of results returned.
        :type page_limit: int, optional
        :param page_cursor: String to query the next page of results.
            This key is provided with each valid response from the API in `meta.page.after`.
        :type page_cursor: str, optional
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

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[ProcessSummary]
        """
        kwargs = self._list_processes_endpoint.default_arguments(kwargs)
        page_size = get_attribute_from_path(kwargs, "page_limit", 1000)
        endpoint = self._list_processes_endpoint
        set_attribute_from_path(kwargs, "page_limit", page_size, endpoint.params_map)
        while True:
            response = endpoint.call_with_http_info(**kwargs)
            for item in get_attribute_from_path(response, "data"):
                yield item
            if len(get_attribute_from_path(response, "data")) < page_size:
                break
            set_attribute_from_path(
                kwargs, "page_cursor", get_attribute_from_path(response, "meta.page.after"), endpoint.params_map
            )
