# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request import CIAppCreatePipelineEventRequest
from datadog_api_client.v2.model.ci_app_pipelines_analytics_aggregate_response import (
    CIAppPipelinesAnalyticsAggregateResponse,
)
from datadog_api_client.v2.model.ci_app_pipelines_aggregate_request import CIAppPipelinesAggregateRequest
from datadog_api_client.v2.model.ci_app_pipeline_events_response import CIAppPipelineEventsResponse
from datadog_api_client.v2.model.ci_app_sort import CIAppSort
from datadog_api_client.v2.model.ci_app_pipeline_event import CIAppPipelineEvent
from datadog_api_client.v2.model.ci_app_pipeline_events_request import CIAppPipelineEventsRequest


class CIVisibilityPipelinesApi:
    """
    Search or aggregate your CI Visibility pipeline events and send them to your Datadog site over HTTP.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._aggregate_ci_app_pipeline_events_endpoint = _Endpoint(
            settings={
                "response_type": (CIAppPipelinesAnalyticsAggregateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/ci/pipelines/analytics/aggregate",
                "operation_id": "aggregate_ci_app_pipeline_events",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CIAppPipelinesAggregateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_ci_app_pipeline_event_endpoint = _Endpoint(
            settings={
                "response_type": (dict,),
                "auth": ["apiKeyAuth"],
                "endpoint_path": "/api/v2/ci/pipeline",
                "operation_id": "create_ci_app_pipeline_event",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CIAppCreatePipelineEventRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._list_ci_app_pipeline_events_endpoint = _Endpoint(
            settings={
                "response_type": (CIAppPipelineEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/ci/pipelines/events",
                "operation_id": "list_ci_app_pipeline_events",
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
                    "openapi_types": (CIAppSort,),
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

        self._search_ci_app_pipeline_events_endpoint = _Endpoint(
            settings={
                "response_type": (CIAppPipelineEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/ci/pipelines/events/search",
                "operation_id": "search_ci_app_pipeline_events",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "openapi_types": (CIAppPipelineEventsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def aggregate_ci_app_pipeline_events(
        self,
        body: CIAppPipelinesAggregateRequest,
    ) -> CIAppPipelinesAnalyticsAggregateResponse:
        """Aggregate pipelines events.

        Use this API endpoint to aggregate CI Visibility pipeline events into buckets of computed metrics and timeseries.

        :type body: CIAppPipelinesAggregateRequest
        :rtype: CIAppPipelinesAnalyticsAggregateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._aggregate_ci_app_pipeline_events_endpoint.call_with_http_info(**kwargs)

    def create_ci_app_pipeline_event(
        self,
        body: CIAppCreatePipelineEventRequest,
    ) -> dict:
        """Send pipeline event.

        Send your pipeline event to your Datadog platform over HTTP. For details about how pipeline executions are modeled and what execution types we support, see `Pipeline Data Model And Execution Types <https://docs.datadoghq.com/continuous_integration/guides/pipeline_data_model/>`_.

        Pipeline events can be submitted with a timestamp that is up to 18 hours in the past.

        :type body: CIAppCreatePipelineEventRequest
        :rtype: dict
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_ci_app_pipeline_event_endpoint.call_with_http_info(**kwargs)

    def list_ci_app_pipeline_events(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[CIAppSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> CIAppPipelineEventsResponse:
        """Get a list of pipelines events.

        List endpoint returns CI Visibility pipeline events that match a `search query <https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/>`_.
        `Results are paginated similarly to logs <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to see your latest pipeline events.

        :param filter_query: Search query following log syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events.
        :type filter_from: datetime, optional
        :param filter_to: Maximum timestamp for requested events.
        :type filter_to: datetime, optional
        :param sort: Order of events in results.
        :type sort: CIAppSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional
        :rtype: CIAppPipelineEventsResponse
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

        return self._list_ci_app_pipeline_events_endpoint.call_with_http_info(**kwargs)

    def list_ci_app_pipeline_events_with_pagination(
        self,
        *,
        filter_query: Union[str, UnsetType] = unset,
        filter_from: Union[datetime, UnsetType] = unset,
        filter_to: Union[datetime, UnsetType] = unset,
        sort: Union[CIAppSort, UnsetType] = unset,
        page_cursor: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
    ) -> collections.abc.Iterable[CIAppPipelineEvent]:
        """Get a list of pipelines events.

        Provide a paginated version of :meth:`list_ci_app_pipeline_events`, returning all items.

        :param filter_query: Search query following log syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events.
        :type filter_from: datetime, optional
        :param filter_to: Maximum timestamp for requested events.
        :type filter_to: datetime, optional
        :param sort: Order of events in results.
        :type sort: CIAppSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[CIAppPipelineEvent]
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
        endpoint = self._list_ci_app_pipeline_events_endpoint
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

    def search_ci_app_pipeline_events(
        self,
        *,
        body: Union[CIAppPipelineEventsRequest, UnsetType] = unset,
    ) -> CIAppPipelineEventsResponse:
        """Search pipelines events.

        List endpoint returns CI Visibility pipeline events that match a `search query <https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/>`_.
        `Results are paginated similarly to logs <https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination>`_.

        Use this endpoint to build complex events filtering and search.

        :type body: CIAppPipelineEventsRequest, optional
        :rtype: CIAppPipelineEventsResponse
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        return self._search_ci_app_pipeline_events_endpoint.call_with_http_info(**kwargs)

    def search_ci_app_pipeline_events_with_pagination(
        self,
        *,
        body: Union[CIAppPipelineEventsRequest, UnsetType] = unset,
    ) -> collections.abc.Iterable[CIAppPipelineEvent]:
        """Search pipelines events.

        Provide a paginated version of :meth:`search_ci_app_pipeline_events`, returning all items.

        :type body: CIAppPipelineEventsRequest, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[CIAppPipelineEvent]
        """
        kwargs: Dict[str, Any] = {}
        if body is not unset:
            kwargs["body"] = body

        local_page_size = get_attribute_from_path(kwargs, "body.page.limit", 10)
        endpoint = self._search_ci_app_pipeline_events_endpoint
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
