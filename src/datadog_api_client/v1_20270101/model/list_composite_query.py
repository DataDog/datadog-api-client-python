# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ListCompositeQuery(ModelComposed):
    def __init__(self, **kwargs):
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

        :param augment_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type augment_query: CompositeSourceSubQuery

        :param join_condition: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_condition: ListAugmentedQueryJoinCondition

        :param segment_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type segment_query: ListSegmentQuerySegmentQuery
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.list_filtered_query import ListFilteredQuery
        from datadog_api_client.v1_20270101.model.list_augmented_query import ListAugmentedQuery
        from datadog_api_client.v1_20270101.model.list_segment_query import ListSegmentQuery

        return {
            "oneOf": [
                ListFilteredQuery,
                ListAugmentedQuery,
                ListSegmentQuery,
            ],
        }
