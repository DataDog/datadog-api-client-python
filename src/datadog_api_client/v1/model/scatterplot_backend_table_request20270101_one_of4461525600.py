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


class ScatterplotBackendTableRequest20270101OneOf4461525600(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "dataset_to_query": (str,),
            "datasets": ([AdvancedQueryDataset],),
            "limit": (float,),
            "projection": (ScatterplotProjection,),
            "request_type": (ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451373184,),
            "response_format": (ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451373984,),
        }

    attribute_map = {
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
        request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451373184,
        response_format: ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451373984,
        limit: Union[float, UnsetType] = unset,
        projection: Union[ScatterplotProjection, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: ScatterplotProjection, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType4451373184

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat4451373984
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if projection is not unset:
            kwargs["projection"] = projection
        super().__init__(kwargs)

        self_.dataset_to_query = dataset_to_query
        self_.datasets = datasets
        self_.request_type = request_type
        self_.response_format = response_format
