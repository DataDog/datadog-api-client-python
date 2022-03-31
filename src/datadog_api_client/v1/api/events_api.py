# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.event_list_response import EventListResponse
from datadog_api_client.v1.model.event_priority import EventPriority
from datadog_api_client.v1.model.event_create_response import EventCreateResponse
from datadog_api_client.v1.model.event_create_request import EventCreateRequest
from datadog_api_client.v1.model.event_response import EventResponse


class EventsApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_event_endpoint = _Endpoint(
            settings={
                "response_type": (EventCreateResponse,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v1/events",
                "operation_id": "create_event",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (EventCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_event_endpoint = _Endpoint(
            settings={
                "response_type": (EventResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/events/{event_id}",
                "operation_id": "get_event",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "event_id": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "event_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_events_endpoint = _Endpoint(
            settings={
                "response_type": (EventListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v1/events",
                "operation_id": "list_events",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "start": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "start",
                    "location": "query",
                },
                "end": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "end",
                    "location": "query",
                },
                "priority": {
                    "openapi_types": (EventPriority,),
                    "attribute": "priority",
                    "location": "query",
                },
                "sources": {
                    "openapi_types": (str,),
                    "attribute": "sources",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": (str,),
                    "attribute": "tags",
                    "location": "query",
                },
                "unaggregated": {
                    "openapi_types": (bool,),
                    "attribute": "unaggregated",
                    "location": "query",
                },
                "exclude_aggregate": {
                    "openapi_types": (bool,),
                    "attribute": "exclude_aggregate",
                    "location": "query",
                },
                "page": {
                    "validation": {
                        "inclusive_maximum": 2147483647,
                    },
                    "openapi_types": (int,),
                    "attribute": "page",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def create_event(self, body, **kwargs):
        """Post an event.

        This endpoint allows you to post events to the stream.
        Tag them, set priority and event aggregate them with other events.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.create_event(body, async_req=True)
        >>> result = thread.get()

        :param body: Event request object
        :type body: EventCreateRequest
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
        :rtype: EventCreateResponse
        """
        kwargs = self._create_event_endpoint.default_arguments(kwargs)
        kwargs["body"] = body

        return self._create_event_endpoint.call_with_http_info(**kwargs)

    def get_event(self, event_id, **kwargs):
        """Get an event.

        This endpoint allows you to query for event details.

        **Note**: If the event you’re querying contains markdown formatting of any kind,
        you may see characters such as `%`,`\\`,`n` in your output.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.get_event(event_id, async_req=True)
        >>> result = thread.get()

        :param event_id: The ID of the event.
        :type event_id: int
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
        :rtype: EventResponse
        """
        kwargs = self._get_event_endpoint.default_arguments(kwargs)
        kwargs["event_id"] = event_id

        return self._get_event_endpoint.call_with_http_info(**kwargs)

    def list_events(self, start, end, **kwargs):
        """Query the event stream.

        The event stream can be queried and filtered by time, priority, sources and tags.

        **Notes**:
        - If the event you’re querying contains markdown formatting of any kind,
        you may see characters such as `%`,`\\`,`n` in your output.

        - This endpoint returns a maximum of `1000` most recent results. To return additional results,
        identify the last timestamp of the last result and set that as the `end` query time to
        paginate the results. You can also use the page parameter to specify which set of `1000` results to return.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_events(start, end, async_req=True)
        >>> result = thread.get()

        :param start: POSIX timestamp.
        :type start: int
        :param end: POSIX timestamp.
        :type end: int
        :param priority: Priority of your events, either `low` or `normal`.
        :type priority: EventPriority, optional
        :param sources: A comma separated string of sources.
        :type sources: str, optional
        :param tags: A comma separated list indicating what tags, if any, should be used to filter the list of monitors by scope.
        :type tags: str, optional
        :param unaggregated: Set unaggregated to `true` to return all events within the specified [`start`,`end`] timeframe.
            Otherwise if an event is aggregated to a parent event with a timestamp outside of the timeframe,
            it won't be available in the output. Aggregated events with `is_aggregate=true` in the response will still be returned unless exclude_aggregate is set to `true.`
        :type unaggregated: bool, optional
        :param exclude_aggregate: Set `exclude_aggregate` to `true` to only return unaggregated events where `is_aggregate=false` in the response. If the `exclude_aggregate` parameter is set to `true`,
            then the unaggregated parameter is ignored and will be `true` by default.
        :type exclude_aggregate: bool, optional
        :param page: By default 1000 results are returned per request. Set page to the number of the page to return with `0` being the first page. The page parameter can only be used
            when either unaggregated or exclude_aggregate is set to `true.`
        :type page: int, optional
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
        :rtype: EventListResponse
        """
        kwargs = self._list_events_endpoint.default_arguments(kwargs)
        kwargs["start"] = start

        kwargs["end"] = end

        return self._list_events_endpoint.call_with_http_info(**kwargs)
