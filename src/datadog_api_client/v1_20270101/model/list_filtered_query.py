# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.composite_events_platform_query import CompositeEventsPlatformQuery
    from datadog_api_client.v1_20270101.model.events_context import EventsContext
    from datadog_api_client.v1_20270101.model.list_filtered_query_data_source import ListFilteredQueryDataSource
    from datadog_api_client.v1_20270101.model.composite_source_sub_query import CompositeSourceSubQuery
    from datadog_api_client.v1_20270101.model.list_filtered_query_filters_items import ListFilteredQueryFiltersItems
    from datadog_api_client.v1_20270101.model.composite_events_platform_sub_query_definition import (
        CompositeEventsPlatformSubQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.composite_referential_data_query import CompositeReferentialDataQuery
    from datadog_api_client.v1_20270101.model.composite_audience_filters_query import CompositeAudienceFiltersQuery


class ListFilteredQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.composite_events_platform_query import CompositeEventsPlatformQuery
        from datadog_api_client.v1_20270101.model.events_context import EventsContext
        from datadog_api_client.v1_20270101.model.list_filtered_query_data_source import ListFilteredQueryDataSource
        from datadog_api_client.v1_20270101.model.composite_source_sub_query import CompositeSourceSubQuery
        from datadog_api_client.v1_20270101.model.list_filtered_query_filters_items import ListFilteredQueryFiltersItems

        return {
            "base_query": (CompositeEventsPlatformQuery,),
            "context": (EventsContext,),
            "data_source": (ListFilteredQueryDataSource,),
            "filter_query": (CompositeSourceSubQuery,),
            "filters": ([ListFilteredQueryFiltersItems],),
            "name": (str,),
        }

    attribute_map = {
        "base_query": "base_query",
        "context": "context",
        "data_source": "data_source",
        "filter_query": "filter_query",
        "filters": "filters",
        "name": "name",
    }

    def __init__(
        self_,
        base_query: CompositeEventsPlatformQuery,
        data_source: ListFilteredQueryDataSource,
        filter_query: Union[
            CompositeSourceSubQuery,
            CompositeEventsPlatformSubQueryDefinition,
            CompositeReferentialDataQuery,
            CompositeAudienceFiltersQuery,
        ],
        filters: List[ListFilteredQueryFiltersItems],
        name: str,
        context: Union[EventsContext, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param base_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_query: CompositeEventsPlatformQuery

        :param context: Test-only generated schema for the dashboard versioning proof of concept.
        :type context: EventsContext, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: ListFilteredQueryDataSource

        :param filter_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter_query: CompositeSourceSubQuery

        :param filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type filters: [ListFilteredQueryFiltersItems]

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if context is not unset:
            kwargs["context"] = context
        super().__init__(kwargs)

        self_.base_query = base_query
        self_.data_source = data_source
        self_.filter_query = filter_query
        self_.filters = filters
        self_.name = name
