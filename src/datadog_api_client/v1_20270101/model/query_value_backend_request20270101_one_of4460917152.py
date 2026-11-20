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
    from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
    from datadog_api_client.v1_20270101.model.comparison_request import ComparisonRequest
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
    from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
        FormulaAndFunctionQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request_any_of_any_of_item_response_format4450609856 import (
        QueryValueBackendRequestAnyOfAnyOfItemResponseFormat4450609856,
    )
    from datadog_api_client.v1_20270101.model.scalar_formula_sort import ScalarFormulaSort
    from datadog_api_client.v1_20270101.model.formula_metrics_query_metrics import FormulaMetricsQueryMetrics
    from datadog_api_client.v1_20270101.model.formula_metrics_query_cloud_cost import FormulaMetricsQueryCloudCost
    from datadog_api_client.v1_20270101.model.formula_metrics_query_datadog_usage import FormulaMetricsQueryDatadogUsage
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition import (
        FormulaAndFunctionEventQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.formula_and_function_process_query_definition import (
        FormulaAndFunctionProcessQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.formula_apm_dependency_stats_query import FormulaApmDependencyStatsQuery
    from datadog_api_client.v1_20270101.model.formula_apm_resource_stats_query import FormulaApmResourceStatsQuery
    from datadog_api_client.v1_20270101.model.formula_apm_metrics_query import FormulaApmMetricsQuery
    from datadog_api_client.v1_20270101.model.formula_incidents_query import FormulaIncidentsQuery
    from datadog_api_client.v1_20270101.model.formula_slo_query import FormulaSloQuery
    from datadog_api_client.v1_20270101.model.formula_case_query import FormulaCaseQuery
    from datadog_api_client.v1_20270101.model.formula_graph_query import FormulaGraphQuery
    from datadog_api_client.v1_20270101.model.formula_user_journey_query import FormulaUserJourneyQuery
    from datadog_api_client.v1_20270101.model.formula_dora_query import FormulaDoraQuery
    from datadog_api_client.v1_20270101.model.formula_change_tracking_query import FormulaChangeTrackingQuery
    from datadog_api_client.v1_20270101.model.formula_detection_rules_query import FormulaDetectionRulesQuery
    from datadog_api_client.v1_20270101.model.aggregate_filtered_query import AggregateFilteredQuery
    from datadog_api_client.v1_20270101.model.aggregate_augmented_query import AggregateAugmentedQuery
    from datadog_api_client.v1_20270101.model.aggregate_segment_query import AggregateSegmentQuery
    from datadog_api_client.v1_20270101.model.formula_dataset_query import FormulaDatasetQuery
    from datadog_api_client.v1_20270101.model.formula_managed_resource_query import FormulaManagedResourceQuery
    from datadog_api_client.v1_20270101.model.formula_reference_table_query import FormulaReferenceTableQuery
    from datadog_api_client.v1_20270101.model.formula_retention_query import FormulaRetentionQuery
    from datadog_api_client.v1_20270101.model.formula_data_quality_metrics_query import FormulaDataQualityMetricsQuery
    from datadog_api_client.v1_20270101.model.formula_product_analytics_extended_query import (
        FormulaProductAnalyticsExtendedQuery,
    )


class QueryValueBackendRequest20270101OneOf4460917152(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.comparison_request import ComparisonRequest
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
        from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
            FormulaAndFunctionQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.query_value_backend_request_any_of_any_of_item_response_format4450609856 import (
            QueryValueBackendRequestAnyOfAnyOfItemResponseFormat4450609856,
        )
        from datadog_api_client.v1_20270101.model.scalar_formula_sort import ScalarFormulaSort

        return {
            "aggregator": (ScalarAggregator,),
            "comparison": (ComparisonRequest,),
            "conditional_formats": ([ThresholdFormattingRule],),
            "formulas": ([WidgetFormula],),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (QueryValueBackendRequestAnyOfAnyOfItemResponseFormat4450609856,),
            "sort": (ScalarFormulaSort,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "comparison": "comparison",
        "conditional_formats": "conditional_formats",
        "formulas": "formulas",
        "queries": "queries",
        "response_format": "response_format",
        "sort": "sort",
    }

    def __init__(
        self_,
        queries: List[
            Union[
                FormulaAndFunctionQueryDefinition,
                FormulaMetricsQueryMetrics,
                FormulaMetricsQueryCloudCost,
                FormulaMetricsQueryDatadogUsage,
                FormulaAndFunctionEventQueryDefinition,
                FormulaAndFunctionProcessQueryDefinition,
                FormulaApmDependencyStatsQuery,
                FormulaApmResourceStatsQuery,
                FormulaApmMetricsQuery,
                FormulaIncidentsQuery,
                FormulaSloQuery,
                FormulaCaseQuery,
                FormulaGraphQuery,
                FormulaUserJourneyQuery,
                FormulaDoraQuery,
                FormulaChangeTrackingQuery,
                FormulaDetectionRulesQuery,
                AggregateFilteredQuery,
                AggregateAugmentedQuery,
                AggregateSegmentQuery,
                FormulaDatasetQuery,
                FormulaManagedResourceQuery,
                FormulaReferenceTableQuery,
                FormulaRetentionQuery,
                FormulaDataQualityMetricsQuery,
                FormulaProductAnalyticsExtendedQuery,
            ]
        ],
        response_format: QueryValueBackendRequestAnyOfAnyOfItemResponseFormat4450609856,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        comparison: Union[ComparisonRequest, UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        formulas: Union[List[WidgetFormula], UnsetType] = unset,
        sort: Union[ScalarFormulaSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param comparison: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparison: ComparisonRequest, optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: QueryValueBackendRequestAnyOfAnyOfItemResponseFormat4450609856

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if comparison is not unset:
            kwargs["comparison"] = comparison
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if formulas is not unset:
            kwargs["formulas"] = formulas
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.queries = queries
        self_.response_format = response_format
