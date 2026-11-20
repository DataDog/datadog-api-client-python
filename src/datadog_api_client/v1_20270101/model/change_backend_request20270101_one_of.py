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
    from datadog_api_client.v1_20270101.model.change_type_options import ChangeTypeOptions
    from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
    from datadog_api_client.v1_20270101.model.order_by_options import OrderByOptions
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
    from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
        FormulaAndFunctionQueryDefinition,
    )
    from datadog_api_client.v1_20270101.model.change_backend_request_any_of_any_of_item_response_format import (
        ChangeBackendRequestAnyOfAnyOfItemResponseFormat,
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


class ChangeBackendRequest20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.change_type_options import ChangeTypeOptions
        from datadog_api_client.v1_20270101.model.widget_formula import WidgetFormula
        from datadog_api_client.v1_20270101.model.order_by_options import OrderByOptions
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
        from datadog_api_client.v1_20270101.model.formula_and_function_query_definition import (
            FormulaAndFunctionQueryDefinition,
        )
        from datadog_api_client.v1_20270101.model.change_backend_request_any_of_any_of_item_response_format import (
            ChangeBackendRequestAnyOfAnyOfItemResponseFormat,
        )
        from datadog_api_client.v1_20270101.model.scalar_formula_sort import ScalarFormulaSort

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
