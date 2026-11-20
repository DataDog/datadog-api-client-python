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


class ChangeBackendRequest20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "change_type": (ChangeTypeOptions,),
            "formulas": ([WidgetFormula],),
            "increase_good": (bool,),
            "limit": (float,),
            "order_by": (OrderByOptions,),
            "order_dir": (QuerySortOrder,),
            "queries": ([FormulaAndFunctionQueryDefinition],),
            "response_format": (ChangeBackendRequestAnyOfAnyOfItemResponseFormat,),
            "show_present": (bool,),
            "sort": (ScalarFormulaSort,),
        }

    attribute_map = {
        "change_type": "change_type",
        "formulas": "formulas",
        "increase_good": "increase_good",
        "limit": "limit",
        "order_by": "order_by",
        "order_dir": "order_dir",
        "queries": "queries",
        "response_format": "response_format",
        "show_present": "show_present",
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
        response_format: ChangeBackendRequestAnyOfAnyOfItemResponseFormat,
        change_type: Union[ChangeTypeOptions, UnsetType] = unset,
        formulas: Union[List[WidgetFormula], UnsetType] = unset,
        increase_good: Union[bool, UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        order_by: Union[OrderByOptions, UnsetType] = unset,
        order_dir: Union[QuerySortOrder, UnsetType] = unset,
        show_present: Union[bool, UnsetType] = unset,
        sort: Union[ScalarFormulaSort, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param change_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type change_type: ChangeTypeOptions, optional

        :param formulas: Test-only generated schema for the dashboard versioning proof of concept.
        :type formulas: [WidgetFormula], optional

        :param increase_good: Test-only generated schema for the dashboard versioning proof of concept.
        :type increase_good: bool, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param order_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type order_by: OrderByOptions, optional

        :param order_dir: Test-only generated schema for the dashboard versioning proof of concept.
        :type order_dir: QuerySortOrder, optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [FormulaAndFunctionQueryDefinition]

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ChangeBackendRequestAnyOfAnyOfItemResponseFormat

        :param show_present: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_present: bool, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: ScalarFormulaSort, optional
        """
        if change_type is not unset:
            kwargs["change_type"] = change_type
        if formulas is not unset:
            kwargs["formulas"] = formulas
        if increase_good is not unset:
            kwargs["increase_good"] = increase_good
        if limit is not unset:
            kwargs["limit"] = limit
        if order_by is not unset:
            kwargs["order_by"] = order_by
        if order_dir is not unset:
            kwargs["order_dir"] = order_dir
        if show_present is not unset:
            kwargs["show_present"] = show_present
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.queries = queries
        self_.response_format = response_format
