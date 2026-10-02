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
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_percentile_aggregation_datadog_metric_measure import (
        ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure,
    )
    from datadog_api_client.v2.model.experiments_metric_property_filter import ExperimentsMetricPropertyFilter
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_percentile_aggregation_warehouse_metric_measure import (
        ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure,
    )


class ExperimentsMetricV2DTODataAttributesPercentileAggregation(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_percentile_aggregation_datadog_metric_measure import (
            ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure,
        )
        from datadog_api_client.v2.model.experiments_metric_property_filter import ExperimentsMetricPropertyFilter
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_percentile_aggregation_warehouse_metric_measure import (
            ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure,
        )

        return {
            "datadog_metric_measure": (ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure,),
            "percentile": (float,),
            "pipeline_column_suffix": (str,),
            "property_filters": ([[ExperimentsMetricPropertyFilter]],),
            "warehouse_metric_measure": (
                ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure,
            ),
        }

    attribute_map = {
        "datadog_metric_measure": "datadog_metric_measure",
        "percentile": "percentile",
        "pipeline_column_suffix": "pipeline_column_suffix",
        "property_filters": "property_filters",
        "warehouse_metric_measure": "warehouse_metric_measure",
    }

    def __init__(
        self_,
        datadog_metric_measure: Union[
            ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure, UnsetType
        ] = unset,
        percentile: Union[float, UnsetType] = unset,
        pipeline_column_suffix: Union[str, UnsetType] = unset,
        property_filters: Union[List[List[ExperimentsMetricPropertyFilter]], UnsetType] = unset,
        warehouse_metric_measure: Union[
            ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Source measure and settings for a percentile metric.

        :param datadog_metric_measure: Datadog source and query that supply values for the metric.
        :type datadog_metric_measure: ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure, optional

        :param percentile: Percentile calculated from the selected measure.
        :type percentile: float, optional

        :param pipeline_column_suffix: Suffix used to identify this value in pipeline output columns.
        :type pipeline_column_suffix: str, optional

        :param property_filters: Filters applied to the metric aggregation.
        :type property_filters: [[ExperimentsMetricPropertyFilter]], optional

        :param warehouse_metric_measure: Warehouse measure that supplies values for the metric.
        :type warehouse_metric_measure: ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure, optional
        """
        if datadog_metric_measure is not unset:
            kwargs["datadog_metric_measure"] = datadog_metric_measure
        if percentile is not unset:
            kwargs["percentile"] = percentile
        if pipeline_column_suffix is not unset:
            kwargs["pipeline_column_suffix"] = pipeline_column_suffix
        if property_filters is not unset:
            kwargs["property_filters"] = property_filters
        if warehouse_metric_measure is not unset:
            kwargs["warehouse_metric_measure"] = warehouse_metric_measure
        super().__init__(kwargs)
