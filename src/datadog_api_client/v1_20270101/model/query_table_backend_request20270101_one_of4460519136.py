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
    from datadog_api_client.v1_20270101.model.cell_display_mode_option import CellDisplayModeOption
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
    from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
        FormulaAndFunctionQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_response_format4450272256 import (
        QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450272256,
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


class QueryTableBackendRequest20270101OneOf4460519136(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.cell_display_mode_option import CellDisplayModeOption
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
        from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
            FormulaAndFunctionQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_response_format4450272256 import (
            QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450272256,
        )
        from datadog_api_client.v1_20270101.model.scalar_formula_sort import ScalarFormulaSort

        return {
            "aggregator": (ScalarAggregator,),
            "alias": (str,),
            "cell_display_mode": ([CellDisplayModeOption],),
            "conditional_formats": ([ThresholdFormattingRule],),
            "formulas": ([WidgetFormula],),
            "limit": (float,),
            "order": (QuerySortOrder,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450272256,),
            "sort": (ScalarFormulaSort,),
            "text_formats": ([[TextFormattingRule]],),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "alias": "alias",
        "cell_display_mode": "cell_display_mode",
        "conditional_formats": "conditional_formats",
        "formulas": "formulas",
        "limit": "limit",
        "order": "order",
        "queries": "queries",
        "response_format": "response_format",
        "sort": "sort",
        "text_formats": "text_formats",
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
        response_format: QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450272256,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        alias: Union[str, UnsetType] = unset,
        cell_display_mode: Union[List[CellDisplayModeOption], UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        formulas: Union[List[WidgetFormula], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        order: Union[QuerySortOrder, UnsetType] = unset,
        sort: Union[ScalarFormulaSort, UnsetType] = unset,
        text_formats: Union[List[List[TextFormattingRule]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param cell_display_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type cell_display_mode: [CellDisplayModeOption], optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450272256

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param text_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_formats: [[TextFormattingRule]], optional
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if alias is not unset:
            kwargs["alias"] = alias
        if cell_display_mode is not unset:
            kwargs["cell_display_mode"] = cell_display_mode
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if formulas is not unset:
            kwargs["formulas"] = formulas
        if limit is not unset:
            kwargs["limit"] = limit
        if order is not unset:
            kwargs["order"] = order
        if sort is not unset:
            kwargs["sort"] = sort
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)

        self_.queries = queries
        self_.response_format = response_format
