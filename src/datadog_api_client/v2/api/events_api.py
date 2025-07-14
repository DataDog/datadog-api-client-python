# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.events_list_response import EventsListResponse
from datadog_api_client.v2.model.events_sort import EventsSort
from datadog_api_client.v2.model.event_response import EventResponse
from datadog_api_client.v2.model.event_create_response_payload import EventCreateResponsePayload
from datadog_api_client.v2.model.event_create_request_payload import EventCreateRequestPayload
from datadog_api_client.v2.model.events_list_request import EventsListRequest


class EventsApi:
    """
    The Event Management API allows you to programmatically post events to the Events Explorer and fetch events from the Events Explorer. See the `Event Management page <https://docs.datadoghq.com/service_management/events/>`_ for more information.

    **Update to Datadog monitor events aggregation_key starting March 1, 2025:** The Datadog monitor events ``aggregation_key`` is unique to each Monitor ID. Starting March 1st, this key will also include Monitor Group, making it unique per *Monitor ID and Monitor Group*. If you're using monitor events ``aggregation_key`` in dashboard queries or the Event API, you must migrate to use ``@monitor.id``. Reach out to `support <https://www.datadoghq.com/support/>`_ if you have any question.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_event_endpoint = _Endpoint(
            settings={
                "response_type": (EventCreateResponsePayload,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/events",
                "operation_id": "create_event",
                "http_method": "POST",
                "version": "v2",
                "servers": [
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "The regional site for customers.",
                                "default_value": "datadoghq.com",
                                "enum_values": [
                                    "datadoghq.com",
                                    "us3.datadoghq.com",
                                    "us5.datadoghq.com",
                                    "ap1.datadoghq.com",
                                    "datadoghq.eu",
                                    "ddog-gov.com",
                                ],
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "event-management-intake",
                            },
                        },
                    },
                    {
                        "url": "{protocol}://{name}",
                        "variables": {
                            "name": {
                                "description": "Full site DNS name.",
                                "default_value": "event-management-intake.datadoghq.com",
                            },
                            "protocol": {
                                "description": "The protocol for accessing the API.",
                                "default_value": "https",
                            },
                        },
                    },
                    {
                        "url": "https://{subdomain}.{site}",
                        "variables": {
                            "site": {
                                "description": "Any Datadog deployment.",
                                "default_value": "datadoghq.com",
                            },
                            "subdomain": {
                                "description": "The subdomain where the API is deployed.",
                                "default_value": "event-management-intake",
                            },
                        },
                    },
                ],
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (EventCreateRequestPayload,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_events_endpoint = _Endpoint(
            settings={
                "response_type": (EventsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/events",
                "operation_id": "list_events",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (str,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (str,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (EventsSort,),
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
            },
            api_client=api_client,
        )

        self._search_events_endpoint = _Endpoint(
            settings={
                "response_type": (EventsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/events/search",
                "operation_id": "search_events",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "openapi_types": (EventsListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_event(
        self,
        body: EventCreateRequestPayload,
    ) -> EventCreateResponsePayload:
        """Post an event.

        This endpoint allows you to publish events.

        **Note:** To utilize this endpoint with our client libraries, please ensure you are using the latest version released on or after July 1, 2025. Earlier versions do not support this functionality.

        ✅ **Only events with the change or alert category** are in General Availability. For change events, see `Change Tracking <https://docs.datadoghq.com/change_tracking>`_ for more details.

        ❌ For use cases involving other event categories, use the V1 endpoint or reach out to `support <https://www.datadoghq.com/support/>`_.

        ❌ Notifications are not yet supported for events sent to this endpoint. Use the V1 endpoint for notification functionality.

        ❌ This endpoint is not available for the Government (US1-FED) site. Contact your account representative for more information.

        :param body: Event creation request payload.
        :type body: EventCreateRequestPayload
        :rtype: EventCreateResponsePayload
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_event_endpoint.call_with_http_info(**kwargs)

    def list_events(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[str, UnsetType] = unset,
        filter_to: Union[str, UnsetType] = unset,
        sort: Union[EventsSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> EventsListResponse:
        """Get a list of events.

        List endpoint returns events that match an events search query.
        `Results are paginated similarly to logs <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to see your latest events.

        :param filter_query: Search query following events syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events, in milliseconds.
        :type filter_from: str, optional
        :param filter_to: Maximum timestamp for requested events, in milliseconds.
        :type filter_to: str, optional
        :param sort: Order of events in results.
        :type sort: EventsSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional
        :rtype: EventsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        return self._list_events_endpoint.call_with_http_info(**kwargs)

    def list_events_with_pagination(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[str, UnsetType] = unset,
        filter_to: Union[str, UnsetType] = unset,
        sort: Union[EventsSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[EventResponse]:
        """Get a list of events.

        Provide a paginated version of :meth:`list_events`, returning all items.

        :param filter_query: Search query following events syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events, in milliseconds.
        :type filter_from: str, optional
        :param filter_to: Maximum timestamp for requested events, in milliseconds.
        :type filter_to: str, optional
        :param sort: Order of events in results.
        :type sort: EventsSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[EventResponse]
        """
        kwargs: Dict[str, Any] = {}
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if sort is not unset:
            kwargs["sort"] = sort

        if page_cursor is not unset:
            kwargs["page_cursor"] = page_cursor

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        local_page_size = get_attribute_from_path(kwargs, "page_limit", 10)
        endpoint = self._list_events_endpoint
        set_attribute_from_path(kwargs, "page_limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "page_cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def search_events(
        self,
        *,
        body: Union[EventsListRequest, UnsetType] = unset,
    ) -> EventsListResponse:
        """Search events.

        List endpoint returns events that match an events search query.
        `Results are paginated similarly to logs <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to build complex events filtering and search.

        :type body: EventsListRequest, optional
        :rtype: EventsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._search_events_endpoint.call_with_http_info(**kwargs)

    def search_events_with_pagination(
        self,
        *,
        body: Union[EventsListRequest, UnsetType] = unset,
    ) -> collections.abc.Iterable[EventResponse]:
        """Search events.

        Provide a paginated version of :meth:`search_events`, returning all items.

        :type body: EventsListRequest, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[EventResponse]
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        local_page_size = get_attribute_from_path(kwargs, "body.page.limit", 10)
        endpoint = self._search_events_endpoint
        set_attribute_from_path(kwargs, "body.page.limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "body.page.cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)
