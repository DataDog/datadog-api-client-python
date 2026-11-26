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
    from datadog_api_client.v1_20270101.model.composite_compute import CompositeCompute
    from datadog_api_client.v1_20270101.model.aggregate_segment_query_data_source import AggregateSegmentQueryDataSource
    from datadog_api_client.v1_20270101.model.composite_group_by import CompositeGroupBy
    from datadog_api_client.v1_20270101.model.aggregate_segment_query_segment_query import (
        AggregateSegmentQuerySegmentQuery,
    )


class AggregateSegmentQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.composite_events_platform_query import CompositeEventsPlatformQuery
        from datadog_api_client.v1_20270101.model.composite_compute import CompositeCompute
        from datadog_api_client.v1_20270101.model.aggregate_segment_query_data_source import (
            AggregateSegmentQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.composite_group_by import CompositeGroupBy
        from datadog_api_client.v1_20270101.model.aggregate_segment_query_segment_query import (
            AggregateSegmentQuerySegmentQuery,
        )

        return {
            "base_query": (CompositeEventsPlatformQuery,),
            "compute": ([CompositeCompute],),
            "data_source": (AggregateSegmentQueryDataSource,),
            "group_by": ([CompositeGroupBy],),
            "name": (str,),
            "segment_query": (AggregateSegmentQuerySegmentQuery,),
        }

    attribute_map = {
        "base_query": "base_query",
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "segment_query": "segment_query",
    }

    def __init__(
        self_,
        base_query: CompositeEventsPlatformQuery,
        compute: List[CompositeCompute],
        data_source: AggregateSegmentQueryDataSource,
        name: str,
        segment_query: AggregateSegmentQuerySegmentQuery,
        group_by: Union[List[CompositeGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param base_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_query: CompositeEventsPlatformQuery

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [CompositeCompute]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: AggregateSegmentQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [CompositeGroupBy], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param segment_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type segment_query: AggregateSegmentQuerySegmentQuery
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.base_query = base_query
        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.segment_query = segment_query
