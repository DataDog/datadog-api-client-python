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


class QueryTableBackendRequest20270101OneOf4460516096(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
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
