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
    from datadog_api_client.v1_20270101.model.composite_source_sub_query import CompositeSourceSubQuery
    from datadog_api_client.v1_20270101.model.composite_source_base_query import CompositeSourceBaseQuery
    from datadog_api_client.v1_20270101.model.composite_compute import CompositeCompute
    from datadog_api_client.v1_20270101.model.aggregate_augmented_query_data_source import (
        AggregateAugmentedQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.composite_group_by import CompositeGroupBy
    from datadog_api_client.v1_20270101.model.aggregate_augmented_query_join_condition import (
        AggregateAugmentedQueryJoinCondition,
    )
    from datadog_api_client.v1_20270101.model.composite_events_platform_sub_query_definition import (
        CompositeEventsPlatformSubQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.composite_referential_data_query import CompositeReferentialDataQuery
    from datadog_api_client.v1_20270101.model.composite_audience_filters_query import CompositeAudienceFiltersQuery
    from datadog_api_client.v1_20270101.model.formula_metrics_query_metrics import FormulaMetricsQueryMetrics
    from datadog_api_client.v1_20270101.model.formula_metrics_query_cloud_cost import FormulaMetricsQueryCloudCost
    from datadog_api_client.v1_20270101.model.formula_metrics_query_datadog_usage import FormulaMetricsQueryDatadogUsage
    from datadog_api_client.v1_20270101.model.composite_events_platform_query_definition import (
        CompositeEventsPlatformQueryDefinition,
    )


class AggregateAugmentedQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.composite_source_sub_query import CompositeSourceSubQuery
        from datadog_api_client.v1_20270101.model.composite_source_base_query import CompositeSourceBaseQuery
        from datadog_api_client.v1_20270101.model.composite_compute import CompositeCompute
        from datadog_api_client.v1_20270101.model.aggregate_augmented_query_data_source import (
            AggregateAugmentedQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.composite_group_by import CompositeGroupBy
        from datadog_api_client.v1_20270101.model.aggregate_augmented_query_join_condition import (
            AggregateAugmentedQueryJoinCondition,
        )

        return {
            "augment_query": (CompositeSourceSubQuery,),
            "base_query": (CompositeSourceBaseQuery,),
            "compute": ([CompositeCompute],),
            "data_source": (AggregateAugmentedQueryDataSource,),
            "group_by": ([CompositeGroupBy],),
            "join_condition": (AggregateAugmentedQueryJoinCondition,),
            "name": (str,),
        }

    attribute_map = {
        "augment_query": "augment_query",
        "base_query": "base_query",
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "join_condition": "join_condition",
        "name": "name",
    }

    def __init__(
        self_,
        augment_query: Union[
            CompositeSourceSubQuery,
            CompositeEventsPlatformSubQueryDefinition,
            CompositeReferentialDataQuery,
            CompositeAudienceFiltersQuery,
        ],
        base_query: Union[
            CompositeSourceBaseQuery,
            FormulaMetricsQueryMetrics,
            FormulaMetricsQueryCloudCost,
            FormulaMetricsQueryDatadogUsage,
            CompositeEventsPlatformQueryDefinition,
        ],
        compute: List[CompositeCompute],
        data_source: AggregateAugmentedQueryDataSource,
        join_condition: AggregateAugmentedQueryJoinCondition,
        name: str,
        group_by: Union[List[CompositeGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param augment_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type augment_query: CompositeSourceSubQuery

        :param base_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type base_query: CompositeSourceBaseQuery

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [CompositeCompute]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: AggregateAugmentedQueryDataSource

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [CompositeGroupBy], optional

        :param join_condition: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_condition: AggregateAugmentedQueryJoinCondition

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.augment_query = augment_query
        self_.base_query = base_query
        self_.compute = compute
        self_.data_source = data_source
        self_.join_condition = join_condition
        self_.name = name
