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
from datadog_api_client.v2.model.spans_aggregate_response import SpansAggregateResponse
from datadog_api_client.v2.model.spans_aggregate_request import SpansAggregateRequest
from datadog_api_client.v2.model.spans_list_response import SpansListResponse
from datadog_api_client.v2.model.spans_sort import SpansSort
from datadog_api_client.v2.model.span import Span
from datadog_api_client.v2.model.spans_list_request import SpansListRequest


class SpansApi:
    """
    Search and aggregate your spans from your Datadog platform over HTTP.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._aggregate_spans_endpoint = _Endpoint(
            settings={
                "response_type": (SpansAggregateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/spans/analytics/aggregate",
                "operation_id": "aggregate_spans",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SpansAggregateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_spans_endpoint = _Endpoint(
            settings={
                "response_type": (SpansListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/spans/events/search",
                "operation_id": "list_spans",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SpansListRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_spans_get_endpoint = _Endpoint(
            settings={
                "response_type": (SpansListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/spans/events",
                "operation_id": "list_spans_get",
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
                    "openapi_types": (SpansSort,),
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

    def aggregate_spans(
        self,
        body: SpansAggregateRequest,
    ) -> SpansAggregateResponse:
        """Aggregate spans.

        The API endpoint to aggregate spans into buckets and compute metrics and timeseries.
        This endpoint is rate limited to ``300`` requests per hour.

        :type body: SpansAggregateRequest
        :rtype: SpansAggregateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._aggregate_spans_endpoint.call_with_http_info(**kwargs)

    def list_spans(
        self,
        body: SpansListRequest,
    ) -> SpansListResponse:
        """Search spans.

        List endpoint returns spans that match a span search query.
        `Results are paginated </logs/guide/collect-multiple-logs-with-pagination?tab=v2api>`_.

        Use this endpoint to build complex spans filtering and search.
        This endpoint is rate limited to ``300`` requests per hour.

        :type body: SpansListRequest
        :rtype: SpansListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._list_spans_endpoint.call_with_http_info(**kwargs)

    def list_spans_with_pagination(
        self,
        body: SpansListRequest,
    ) -> collections.abc.Iterable[Span]:
        """Search spans.

        Provide a paginated version of :meth:`list_spans`, returning all items.

        :type body: SpansListRequest

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[Span]
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        local_page_size = get_attribute_from_path(kwargs, "body.data.attributes.page.limit", 10)
        endpoint = self._list_spans_endpoint
        set_attribute_from_path(kwargs, "body.data.attributes.page.limit", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "cursor_param": "body.data.attributes.page.cursor",
            "cursor_path": "meta.page.after",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_spans_get(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[str, UnsetType] = unset,
        filter_to: Union[str, UnsetType] = unset,
        sort: Union[SpansSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> SpansListResponse:
        """Get a list of spans.

        List endpoint returns spans that match a span search query.
        `Results are paginated </logs/guide/collect-multiple-logs-with-pagination?tab=v2api>`_.

        Use this endpoint to see your latest spans.
        This endpoint is rate limited to ``300`` requests per hour.

        :param filter_query: Search query following spans syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds).
        :type filter_from: str, optional
        :param filter_to: Maximum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds).
        :type filter_to: str, optional
        :param sort: Order of spans in results.
        :type sort: SpansSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of spans in the response.
        :type page_limit: int, optional
        :rtype: SpansListResponse
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

        return self._list_spans_get_endpoint.call_with_http_info(**kwargs)

    def list_spans_get_with_pagination(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[str, UnsetType] = unset,
        filter_to: Union[str, UnsetType] = unset,
        sort: Union[SpansSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[Span]:
        """Get a list of spans.

        Provide a paginated version of :meth:`list_spans_get`, returning all items.

        :param filter_query: Search query following spans syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds).
        :type filter_from: str, optional
        :param filter_to: Maximum timestamp for requested spans. Supports date-time ISO8601, date math, and regular timestamps (milliseconds).
        :type filter_to: str, optional
        :param sort: Order of spans in results.
        :type sort: SpansSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of spans in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[Span]
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
        endpoint = self._list_spans_get_endpoint
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
