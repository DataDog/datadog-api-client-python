# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class QueryValueBackendRequest20270101OneOf4460917152(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
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
