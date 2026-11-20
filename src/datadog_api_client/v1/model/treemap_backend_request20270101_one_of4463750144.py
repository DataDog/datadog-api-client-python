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


class TreemapBackendRequest20270101OneOf4463750144(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "formulas": ([WidgetFormula],),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453527168,),
            "sort": (ScalarFormulaSort,),
            "style": (TreemapRequestStyle,),
        }

    attribute_map = {
        "formulas": "formulas",
        "queries": "queries",
        "response_format": "response_format",
        "sort": "sort",
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
        response_format: TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453527168,
        formulas: Union[List[WidgetFormula], UnsetType] = unset,
        sort: Union[ScalarFormulaSort, UnsetType] = unset,
        style: Union[TreemapRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TreemapBackendRequestAnyOfAnyOfItemResponseFormat4453527168

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TreemapRequestStyle, optional
        """
        if formulas is not unset:
            kwargs["formulas"] = formulas
        if sort is not unset:
            kwargs["sort"] = sort
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.queries = queries
        self_.response_format = response_format
