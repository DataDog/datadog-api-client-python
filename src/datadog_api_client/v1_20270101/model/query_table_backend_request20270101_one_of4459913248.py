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
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
    from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of_query import (
        QueryTableBackendRequest20270101OneOfQuery,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_request_type4449627456 import (
        QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_response_format4449627776 import (
        QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4449627776,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_projection import ScatterplotProjection
    from datadog_api_client.v1_20270101.model.tree_data_projection_bar_chart import TreeDataProjectionBarChart
    from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst import TreeDataProjectionSunburst
    from datadog_api_client.v1_20270101.model.tree_data_projection_toplist import TreeDataProjectionToplist
    from datadog_api_client.v1_20270101.model.tree_data_projection_treemap import TreeDataProjectionTreemap
    from datadog_api_client.v1_20270101.model.query_value_projection import QueryValueProjection
    from datadog_api_client.v1_20270101.model.query_table_projection import QueryTableProjection
    from datadog_api_client.v1_20270101.model.run_chart_projection import RunChartProjection
    from datadog_api_client.v1_20270101.model.structured_analysis_query import StructuredAnalysisQuery
    from datadog_api_client.v1_20270101.model.sampled_analysis_query import SampledAnalysisQuery


class QueryTableBackendRequest20270101OneOf4459913248(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.cell_display_mode_option import CellDisplayModeOption
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
        from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
        from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of_query import (
            QueryTableBackendRequest20270101OneOfQuery,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_request_type4449627456 import (
            QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_response_format4449627776 import (
            QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4449627776,
        )

        return {
            "aggregator": (ScalarAggregator,),
            "alias": (str,),
            "cell_display_mode": ([CellDisplayModeOption],),
            "conditional_formats": ([ThresholdFormattingRule],),
            "limit": (float,),
            "order": (QuerySortOrder,),
            "projection": (TabularProjection,),
            "query": (QueryTableBackendRequest20270101OneOfQuery,),
            "request_type": (QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456,),
            "response_format": (QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4449627776,),
            "text_formats": ([[TextFormattingRule]],),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "alias": "alias",
        "cell_display_mode": "cell_display_mode",
        "conditional_formats": "conditional_formats",
        "limit": "limit",
        "order": "order",
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
        "response_format": "response_format",
        "text_formats": "text_formats",
    }

    def __init__(
        self_,
        query: Union[QueryTableBackendRequest20270101OneOfQuery, StructuredAnalysisQuery, SampledAnalysisQuery],
        request_type: QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456,
        response_format: QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4449627776,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        alias: Union[str, UnsetType] = unset,
        cell_display_mode: Union[List[CellDisplayModeOption], UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        order: Union[QuerySortOrder, UnsetType] = unset,
        projection: Union[
            TabularProjection,
            ScatterplotProjection,
            TreeDataProjectionBarChart,
            TreeDataProjectionSunburst,
            TreeDataProjectionToplist,
            TreeDataProjectionTreemap,
            QueryValueProjection,
            QueryTableProjection,
            RunChartProjection,
            UnsetType,
        ] = unset,
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

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: QueryTableBackendRequest20270101OneOfQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4449627776

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
        if projection is not unset:
            kwargs["projection"] = projection
        if text_formats is not unset:
            kwargs["text_formats"] = text_formats
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
        self_.response_format = response_format
