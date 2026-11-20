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
    from datadog_api_client.v1_20270101.model.composite_stream_request_column import CompositeStreamRequestColumn
    from datadog_api_client.v1_20270101.model.list_composite_query import ListCompositeQuery
    from datadog_api_client.v1_20270101.model.composite_stream_request_request_type import (
        CompositeStreamRequestRequestType,
    )
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort
    from datadog_api_client.v1_20270101.model.list_filtered_query import ListFilteredQuery
    from datadog_api_client.v1_20270101.model.list_augmented_query import ListAugmentedQuery
    from datadog_api_client.v1_20270101.model.list_segment_query import ListSegmentQuery


class CompositeStreamRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.composite_stream_request_column import CompositeStreamRequestColumn
        from datadog_api_client.v1_20270101.model.list_composite_query import ListCompositeQuery
        from datadog_api_client.v1_20270101.model.composite_stream_request_request_type import (
            CompositeStreamRequestRequestType,
        )
        from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort

        return {
            "columns": ([CompositeStreamRequestColumn],),
            "query": (ListCompositeQuery,),
            "request_type": (CompositeStreamRequestRequestType,),
            "sort": (ListStreamSort,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "request_type": "request_type",
        "sort": "sort",
    }

    def __init__(
        self_,
        columns: List[CompositeStreamRequestColumn],
        query: Union[ListCompositeQuery, ListFilteredQuery, ListAugmentedQuery, ListSegmentQuery],
        request_type: CompositeStreamRequestRequestType,
        sort: Union[ListStreamSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [CompositeStreamRequestColumn]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: ListCompositeQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: CompositeStreamRequestRequestType

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ListStreamSort, optional
        """
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.request_type = request_type
