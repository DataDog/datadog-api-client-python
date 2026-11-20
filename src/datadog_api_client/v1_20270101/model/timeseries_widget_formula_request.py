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
    from datadog_api_client.v1_20270101.model.widget_display_type import WidgetDisplayType
    from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
    from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import TimeseriesWidgetExpressionAlias
    from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
        FormulaAndFunctionQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_formula_request_response_format import (
        TimeseriesWidgetFormulaRequestResponseFormat,
    )
    from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle
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


class TimeseriesWidgetFormulaRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_display_type import WidgetDisplayType
        from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
        from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import (
            TimeseriesWidgetExpressionAlias,
        )
        from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
            FormulaAndFunctionQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_formula_request_response_format import (
            TimeseriesWidgetFormulaRequestResponseFormat,
        )
        from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle

        return {
            "display_type": (WidgetDisplayType,),
            "formulas": ([WidgetFormula],),
            "metadata": ([TimeseriesWidgetExpressionAlias],),
            "on_right_yaxis": (bool,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (TimeseriesWidgetFormulaRequestResponseFormat,),
            "style": (TimeseriesRequestStyle,),
        }

    attribute_map = {
        "display_type": "display_type",
        "formulas": "formulas",
        "metadata": "metadata",
        "on_right_yaxis": "on_right_yaxis",
        "queries": "queries",
        "response_format": "response_format",
        "style": "style",
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
        response_format: TimeseriesWidgetFormulaRequestResponseFormat,
        display_type: Union[WidgetDisplayType, UnsetType] = unset,
        formulas: Union[List[WidgetFormula], UnsetType] = unset,
        metadata: Union[List[TimeseriesWidgetExpressionAlias], UnsetType] = unset,
        on_right_yaxis: Union[bool, UnsetType] = unset,
        style: Union[TimeseriesRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param display_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_type: WidgetDisplayType, optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param metadata: Test-only generated schema for the dashboard versioning proof of concept.
        :type metadata: [TimeseriesWidgetExpressionAlias], optional

        :param on_right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type on_right_yaxis: bool, optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TimeseriesWidgetFormulaRequestResponseFormat

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TimeseriesRequestStyle, optional
        """
        if display_type is not unset:
            kwargs["display_type"] = display_type
        if formulas is not unset:
            kwargs["formulas"] = formulas
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if on_right_yaxis is not unset:
            kwargs["on_right_yaxis"] = on_right_yaxis
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.queries = queries
        self_.response_format = response_format
