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
    from datadog_api_client.v1_20270101.model.advanced_query_dataset import AdvancedQueryDataset
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
    from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
    from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_request_type4450135840 import (
        QueryTableBackendRequestAnyOfAnyOfItemRequestType4450135840,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_response_format4450136640 import (
        QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450136640,
    )
    from datadog_api_client.v1_20270101.model.event_platform_dataset_definition import EventPlatformDatasetDefinition
    from datadog_api_client.v1_20270101.model.referential_dataset_reference_table import (
        ReferentialDatasetReferenceTable,
    )
    from datadog_api_client.v1_20270101.model.referential_dataset_managed_resource import (
        ReferentialDatasetManagedResource,
    )
    from datadog_api_client.v1_20270101.model.actions_datastore_dataset import ActionsDatastoreDataset
    from datadog_api_client.v1_20270101.model.metric_dataset_cloud_cost_scalar import MetricDatasetCloudCostScalar
    from datadog_api_client.v1_20270101.model.metric_dataset_metric_scalar import MetricDatasetMetricScalar
    from datadog_api_client.v1_20270101.model.formula_dataset import FormulaDataset
    from datadog_api_client.v1_20270101.model.analysis_dataset import AnalysisDataset
    from datadog_api_client.v1_20270101.model.published_analysis import PublishedAnalysis
    from datadog_api_client.v1_20270101.model.snowflake_query_dataset import SnowflakeQueryDataset
    from datadog_api_client.v1_20270101.model.big_query_dataset import BigQueryDataset
    from datadog_api_client.v1_20270101.model.product_analytics_journey_dataset import ProductAnalyticsJourneyDataset
    from datadog_api_client.v1_20270101.model.historical_discovered_processes_dataset import (
        HistoricalDiscoveredProcessesDataset,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_projection import ScatterplotProjection
    from datadog_api_client.v1_20270101.model.tree_data_projection_bar_chart import TreeDataProjectionBarChart
    from datadog_api_client.v1_20270101.model.tree_data_projection_sunburst import TreeDataProjectionSunburst
    from datadog_api_client.v1_20270101.model.tree_data_projection_toplist import TreeDataProjectionToplist
    from datadog_api_client.v1_20270101.model.tree_data_projection_treemap import TreeDataProjectionTreemap
    from datadog_api_client.v1_20270101.model.query_value_projection import QueryValueProjection
    from datadog_api_client.v1_20270101.model.query_table_projection import QueryTableProjection
    from datadog_api_client.v1_20270101.model.run_chart_projection import RunChartProjection


class QueryTableBackendRequest20270101OneOf4460516096(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator
        from datadog_api_client.v1_20270101.model.cell_display_mode_option import CellDisplayModeOption
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.advanced_query_dataset import AdvancedQueryDataset
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
        from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
        from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_request_type4450135840 import (
            QueryTableBackendRequestAnyOfAnyOfItemRequestType4450135840,
        )
        from datadog_api_client.v1_20270101.model.query_table_backend_request_any_of_any_of_item_response_format4450136640 import (
            QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450136640,
        )

        return {
            "aggregator": (ScalarAggregator,),
            "alias": (str,),
            "cell_display_mode": ([CellDisplayModeOption],),
            "conditional_formats": ([ThresholdFormattingRule],),
            "dataset_to_query": (str,),
            "datasets": ([AdvancedQueryDataset],),
            "limit": (float,),
            "order": (QuerySortOrder,),
            "projection": (TabularProjection,),
            "request_type": (QueryTableBackendRequestAnyOfAnyOfItemRequestType4450135840,),
            "response_format": (QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450136640,),
            "text_formats": ([[TextFormattingRule]],),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "alias": "alias",
        "cell_display_mode": "cell_display_mode",
        "conditional_formats": "conditional_formats",
        "dataset_to_query": "dataset_to_query",
        "datasets": "datasets",
        "limit": "limit",
        "order": "order",
        "projection": "projection",
        "request_type": "request_type",
        "response_format": "response_format",
        "text_formats": "text_formats",
    }

    def __init__(
        self_,
        dataset_to_query: str,
        datasets: List[
            Union[
                AdvancedQueryDataset,
                EventPlatformDatasetDefinition,
                ReferentialDatasetReferenceTable,
                ReferentialDatasetManagedResource,
                ActionsDatastoreDataset,
                MetricDatasetCloudCostScalar,
                MetricDatasetMetricScalar,
                FormulaDataset,
                AnalysisDataset,
                PublishedAnalysis,
                SnowflakeQueryDataset,
                BigQueryDataset,
                ProductAnalyticsJourneyDataset,
                HistoricalDiscoveredProcessesDataset,
            ]
        ],
        request_type: QueryTableBackendRequestAnyOfAnyOfItemRequestType4450135840,
        response_format: QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450136640,
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

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: QueryTableBackendRequestAnyOfAnyOfItemRequestType4450135840

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: QueryTableBackendRequestAnyOfAnyOfItemResponseFormat4450136640

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

        self_.dataset_to_query = dataset_to_query
        self_.datasets = datasets
        self_.request_type = request_type
        self_.response_format = response_format
