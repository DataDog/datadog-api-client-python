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
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.advanced_query_dataset import AdvancedQueryDataset
    from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
    from datadog_api_client.v1_20270101.model.toplist_backend_request_any_of_any_of_item_request_type import (
        ToplistBackendRequestAnyOfAnyOfItemRequestType,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request_any_of_any_of_item_response_format import (
        ToplistBackendRequestAnyOfAnyOfItemResponseFormat,
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


class ToplistBackendRequest20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.advanced_query_dataset import AdvancedQueryDataset
        from datadog_api_client.v1_20270101.model.tabular_projection import TabularProjection
        from datadog_api_client.v1_20270101.model.toplist_backend_request_any_of_any_of_item_request_type import (
            ToplistBackendRequestAnyOfAnyOfItemRequestType,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_request_any_of_any_of_item_response_format import (
            ToplistBackendRequestAnyOfAnyOfItemResponseFormat,
        )

        return {
            "conditional_formats": ([ThresholdFormattingRule],),
            "dataset_to_query": (str,),
            "datasets": ([AdvancedQueryDataset],),
            "limit": (float,),
            "projection": (TabularProjection,),
            "request_type": (ToplistBackendRequestAnyOfAnyOfItemRequestType,),
            "response_format": (ToplistBackendRequestAnyOfAnyOfItemResponseFormat,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "dataset_to_query": "dataset_to_query",
        "datasets": "datasets",
        "limit": "limit",
        "projection": "projection",
        "request_type": "request_type",
        "response_format": "response_format",
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
        request_type: ToplistBackendRequestAnyOfAnyOfItemRequestType,
        response_format: ToplistBackendRequestAnyOfAnyOfItemResponseFormat,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
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
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TabularProjection, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: ToplistBackendRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ToplistBackendRequestAnyOfAnyOfItemResponseFormat
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if limit is not unset:
            kwargs["limit"] = limit
        if projection is not unset:
            kwargs["projection"] = projection
        super().__init__(kwargs)

        self_.dataset_to_query = dataset_to_query
        self_.datasets = datasets
        self_.request_type = request_type
        self_.response_format = response_format
