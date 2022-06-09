# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    datetime,
    set_attribute_from_path,
    get_attribute_from_path,
)
from datadog_api_client.v2.model.rum_analytics_aggregate_response import RUMAnalyticsAggregateResponse
from datadog_api_client.v2.model.rum_aggregate_request import RUMAggregateRequest
from datadog_api_client.v2.model.rum_events_response import RUMEventsResponse
from datadog_api_client.v2.model.rum_sort import RUMSort
from datadog_api_client.v2.model.rum_search_events_request import RUMSearchEventsRequest


class RUMApi:
    """
    Search or aggregate your RUM events over HTTP.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._aggregate_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMAnalyticsAggregateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/analytics/aggregate",
                "operation_id": "aggregate_rum_events",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RUMAggregateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/events",
                "operation_id": "list_rum_events",
                "http_method": "GET",
                "version": "v2",
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
                    "openapi_types": (RUMSort,),
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

        self._search_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/events/search",
                "operation_id": "search_rum_events",
                "http_method": "POST",
                "version": "v2",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (RUMSearchEventsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def aggregate_rum_events(self, body, **kwargs):
        """Aggregate RUM events.

        The API endpoint to aggregate RUM events into buckets of computed metrics and timeseries.

        :type body: RUMAggregateRequest
        :rtype: RUMAnalyticsAggregateResponse
        """
        kwargs["body"] = body

        return self._aggregate_rum_events_endpoint.call_with_http_info(**kwargs)

    def list_rum_events(self, **kwargs):
        """Get a list of RUM events.

        List endpoint returns events that match a RUM search query.
        `Results are paginated <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to see your latest RUM events.

        :param filter_query: Search query following RUM syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events.
        :type filter_from: datetime, optional
        :param filter_to: Maximum timestamp for requested events.
        :type filter_to: datetime, optional
        :param sort: Order of events in results.
        :type sort: RUMSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional
        :rtype: RUMEventsResponse
        """
        return self._list_rum_events_endpoint.call_with_http_info(**kwargs)

    def list_rum_events_with_pagination(self, **kwargs):
        """Get a list of RUM events.

        Provide a paginated version of :meth:`list_rum_events`, returning all items.

        :param filter_query: Search query following RUM syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events.
        :type filter_from: datetime, optional
        :param filter_to: Maximum timestamp for requested events.
        :type filter_to: datetime, optional
        :param sort: Order of events in results.
        :type sort: RUMSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[RUMEvent]
        """
        page_size = get_attribute_from_path(kwargs, "page_limit", 10)
        endpoint = self._list_rum_events_endpoint
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

    def search_rum_events(self, body, **kwargs):
        """Search RUM events.

        List endpoint returns RUM events that match a RUM search query.
        `Results are paginated <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to build complex RUM events filtering and search.

        :type body: RUMSearchEventsRequest
        :rtype: RUMEventsResponse
        """
        kwargs["body"] = body

        return self._search_rum_events_endpoint.call_with_http_info(**kwargs)

    def search_rum_events_with_pagination(self, body, **kwargs):
        """Search RUM events.

        Provide a paginated version of :meth:`search_rum_events`, returning all items.

        :type body: RUMSearchEventsRequest

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[RUMEvent]
        """
        kwargs["body"] = body

        page_size = get_attribute_from_path(kwargs, "body.page.limit", 10)
        endpoint = self._search_rum_events_endpoint
        set_attribute_from_path(kwargs, "body.page.limit", page_size, endpoint.params_map)
        while True:
            response = endpoint.call_with_http_info(**kwargs)
            for item in get_attribute_from_path(response, "data"):
                yield item
            if len(get_attribute_from_path(response, "data")) < page_size:
                break
            set_attribute_from_path(
                kwargs, "body.page.cursor", get_attribute_from_path(response, "meta.page.after"), endpoint.params_map
            )
