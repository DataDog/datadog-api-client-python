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
    from datadog_api_client.v1_20270101.model.table_column import TableColumn
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
    from datadog_api_client.v1_20270101.model.guided_table_query import GuidedTableQuery
    from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_request_type4450129280 import (
        QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280,
    )
    from datadog_api_client.v1_20270101.model.table_rows import TableRows
    from datadog_api_client.v1_20270101.model.compute_table_column import ComputeTableColumn
    from datadog_api_client.v1_20270101.model.preset_period_table_column import PresetPeriodTableColumn
    from datadog_api_client.v1_20270101.model.formula_table_column import FormulaTableColumn
    from datadog_api_client.v1_20270101.model.reference_table_column import ReferenceTableColumn
    from datadog_api_client.v1_20270101.model.metrics_like_query_fragment_metrics import MetricsLikeQueryFragmentMetrics
    from datadog_api_client.v1_20270101.model.metrics_like_query_fragment_cloud_cost import (
        MetricsLikeQueryFragmentCloudCost,
    )
    from datadog_api_client.v1_20270101.model.events_query_fragment_definition import EventsQueryFragmentDefinition
    from datadog_api_client.v1_20270101.model.referential_query_fragment_reference_table import (
        ReferentialQueryFragmentReferenceTable,
    )
    from datadog_api_client.v1_20270101.model.referential_query_fragment_managed_resource import (
        ReferentialQueryFragmentManagedResource,
    )
    from datadog_api_client.v1_20270101.model.published_analysis_query_fragment import PublishedAnalysisQueryFragment
    from datadog_api_client.v1_20270101.model.apm_metrics_query_fragment import ApmMetricsQueryFragment


class QueryTableBackendRequest20270101OneOf4460313504(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.cell_display_mode_option import CellDisplayModeOption
        from datadog_api_client.v1_20270101.model.table_column import TableColumn
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
        from datadog_api_client.v1_20270101.model.guided_table_query import GuidedTableQuery
        from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_request_type4450129280 import (
            QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280,
        )
        from datadog_api_client.v1_20270101.model.table_rows import TableRows

        return {
            "aggregator": (ScalarAggregator,),
            "alias": (str,),
            "cell_display_mode": ([CellDisplayModeOption],),
            "columns": ([TableColumn],),
            "conditional_formats": ([ThresholdFormattingRule],),
            "limit": (float,),
            "order": (QuerySortOrder,),
            "queries": ([GuidedTableQuery],),
            "request_type": (QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280,),
            "rows": (TableRows,),
            "text_formats": ([[TextFormattingRule]],),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "alias": "alias",
        "cell_display_mode": "cell_display_mode",
        "columns": "columns",
        "conditional_formats": "conditional_formats",
        "limit": "limit",
        "order": "order",
        "queries": "queries",
        "request_type": "request_type",
        "rows": "rows",
        "text_formats": "text_formats",
    }

    def __init__(
        self_,
        columns: List[
            Union[TableColumn, ComputeTableColumn, PresetPeriodTableColumn, FormulaTableColumn, ReferenceTableColumn]
        ],
        queries: List[
            Union[
                GuidedTableQuery,
                MetricsLikeQueryFragmentMetrics,
                MetricsLikeQueryFragmentCloudCost,
                EventsQueryFragmentDefinition,
                ReferentialQueryFragmentReferenceTable,
                ReferentialQueryFragmentManagedResource,
                PublishedAnalysisQueryFragment,
                ApmMetricsQueryFragment,
            ]
        ],
        request_type: QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280,
        rows: TableRows,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        alias: Union[str, UnsetType] = unset,
        cell_display_mode: Union[List[CellDisplayModeOption], UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        order: Union[QuerySortOrder, UnsetType] = unset,
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

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [TableColumn]

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional

        :param queries: Test-only generated schema for the dashboard versioning proof of concept.
        :type queries: [GuidedTableQuery]

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: QueryTableBackendRequestAnyOfAnyOfItemRequestType4450129280

        :param rows: Test-only generated schema for the dashboard versioning proof of concept.
        :type rows: TableRows

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
        if limit is not unset:
            kwargs["limit"] = limit
        if order is not unset:
            kwargs["order"] = order
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)

        self_.columns = columns
        self_.queries = queries
        self_.request_type = request_type
        self_.rows = rows
