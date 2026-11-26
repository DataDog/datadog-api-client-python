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
    from datadog_api_client.v1_20270101.model.advanced_query_dataset import AdvancedQueryDataset
    from datadog_api_client.v1_20270101.model.widget_display_type import WidgetDisplayType
    from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import TimeseriesWidgetExpressionAlias
    from datadog_api_client.v1_20270101.model.timeseries_projection import TimeseriesProjection
    from datadog_api_client.v1_20270101.model.timeseries_widget_advanced_query_request_request_type import (
        TimeseriesWidgetAdvancedQueryRequestRequestType,
    )
    from datadog_api_client.v1_20270101.model.timeseries_widget_advanced_query_request_response_format import (
        TimeseriesWidgetAdvancedQueryRequestResponseFormat,
    )
    from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle
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


class TimeseriesWidgetAdvancedQueryRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.advanced_query_dataset import AdvancedQueryDataset
        from datadog_api_client.v1_20270101.model.widget_display_type import WidgetDisplayType
        from datadog_api_client.v1_20270101.model.timeseries_widget_expression_alias import (
            TimeseriesWidgetExpressionAlias,
        )
        from datadog_api_client.v1_20270101.model.timeseries_projection import TimeseriesProjection
        from datadog_api_client.v1_20270101.model.timeseries_widget_advanced_query_request_request_type import (
            TimeseriesWidgetAdvancedQueryRequestRequestType,
        )
        from datadog_api_client.v1_20270101.model.timeseries_widget_advanced_query_request_response_format import (
            TimeseriesWidgetAdvancedQueryRequestResponseFormat,
        )
        from datadog_api_client.v1_20270101.model.timeseries_request_style import TimeseriesRequestStyle

        return {
            "dataset_to_query": (str,),
            "datasets": ([AdvancedQueryDataset],),
            "display_type": (WidgetDisplayType,),
            "limit": (float,),
            "metadata": ([TimeseriesWidgetExpressionAlias],),
            "on_right_yaxis": (bool,),
            "projection": (TimeseriesProjection,),
            "request_type": (TimeseriesWidgetAdvancedQueryRequestRequestType,),
            "response_format": (TimeseriesWidgetAdvancedQueryRequestResponseFormat,),
            "style": (TimeseriesRequestStyle,),
        }

    attribute_map = {
        "dataset_to_query": "dataset_to_query",
        "datasets": "datasets",
        "display_type": "display_type",
        "limit": "limit",
        "metadata": "metadata",
        "on_right_yaxis": "on_right_yaxis",
        "projection": "projection",
        "request_type": "request_type",
        "response_format": "response_format",
        "style": "style",
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
        request_type: TimeseriesWidgetAdvancedQueryRequestRequestType,
        response_format: TimeseriesWidgetAdvancedQueryRequestResponseFormat,
        display_type: Union[WidgetDisplayType, UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        metadata: Union[List[TimeseriesWidgetExpressionAlias], UnsetType] = unset,
        on_right_yaxis: Union[bool, UnsetType] = unset,
        projection: Union[TimeseriesProjection, UnsetType] = unset,
        style: Union[TimeseriesRequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param dataset_to_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_to_query: str

        :param datasets: Test-only generated schema for the dashboard versioning proof of concept.
        :type datasets: [AdvancedQueryDataset]

        :param display_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_type: WidgetDisplayType, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param metadata: Test-only generated schema for the dashboard versioning proof of concept.
        :type metadata: [TimeseriesWidgetExpressionAlias], optional

        :param on_right_yaxis: Test-only generated schema for the dashboard versioning proof of concept.
        :type on_right_yaxis: bool, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: TimeseriesProjection, optional

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: TimeseriesWidgetAdvancedQueryRequestRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: TimeseriesWidgetAdvancedQueryRequestResponseFormat

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: TimeseriesRequestStyle, optional
        """
        if display_type is not unset:
            kwargs["display_type"] = display_type
        if limit is not unset:
            kwargs["limit"] = limit
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if on_right_yaxis is not unset:
            kwargs["on_right_yaxis"] = on_right_yaxis
        if projection is not unset:
            kwargs["projection"] = projection
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.dataset_to_query = dataset_to_query
        self_.datasets = datasets
        self_.request_type = request_type
        self_.response_format = response_format
