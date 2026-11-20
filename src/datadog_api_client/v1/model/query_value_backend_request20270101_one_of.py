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


class QueryValueBackendRequest20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "aggregator": (ScalarAggregator,),
            "comparison": (ComparisonRequest,),
            "conditional_formats": ([ThresholdFormattingRule],),
            "dataset_to_query": (str,),
            "datasets": ([AdvancedQueryDataset],),
            "limit": (float,),
            "projection": (TabularProjection,),
            "request_type": (QueryValueBackendRequestAnyOfAnyOfItemRequestType,),
            "response_format": (QueryValueBackendRequestAnyOfAnyOfItemResponseFormat,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "comparison": "comparison",
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
        request_type: QueryValueBackendRequestAnyOfAnyOfItemRequestType,
        response_format: QueryValueBackendRequestAnyOfAnyOfItemResponseFormat,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        comparison: Union[ComparisonRequest, UnsetType] = unset,
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

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param comparison: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparison: ComparisonRequest, optional

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
        :type request_type: QueryValueBackendRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: QueryValueBackendRequestAnyOfAnyOfItemResponseFormat
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if comparison is not unset:
            kwargs["comparison"] = comparison
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
