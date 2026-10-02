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


class ExperimentsMetricV2DTODataAttributesNumeratorAggregation(ModelNormal):
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
            "aging_threshold_days": (int,),
            "datadog_metric_measure": (ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure,),
            "enable_aging_subject_filter": (bool,),
            "operation": (str,),
            "pipeline_column_suffix": (str,),
            "property_filters": ([[ExperimentsMetricPropertyFilter]],),
            "threshold_aggregation_type": (str,),
            "threshold_breach_value": (float,),
            "threshold_comparison_operator": (str,),
            "threshold_timeframe_dimension": (str,),
            "threshold_timeframe_value": (float,),
            "timeframe_end_value": (float,),
            "timeframe_start_value": (float,),
            "timeframe_unit": (str,),
            "warehouse_metric_measure": (
                ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure,
            ),
            "winsor_lower_fixed_value": (float,),
            "winsor_lower_percentile": (float,),
            "winsor_upper_fixed_value": (float,),
            "winsor_upper_percentile": (float,),
            "winsorization_strategy": (str,),
        }

    attribute_map = {
        "aging_threshold_days": "aging_threshold_days",
        "datadog_metric_measure": "datadog_metric_measure",
        "enable_aging_subject_filter": "enable_aging_subject_filter",
        "operation": "operation",
        "pipeline_column_suffix": "pipeline_column_suffix",
        "property_filters": "property_filters",
        "threshold_aggregation_type": "threshold_aggregation_type",
        "threshold_breach_value": "threshold_breach_value",
        "threshold_comparison_operator": "threshold_comparison_operator",
        "threshold_timeframe_dimension": "threshold_timeframe_dimension",
        "threshold_timeframe_value": "threshold_timeframe_value",
        "timeframe_end_value": "timeframe_end_value",
        "timeframe_start_value": "timeframe_start_value",
        "timeframe_unit": "timeframe_unit",
        "warehouse_metric_measure": "warehouse_metric_measure",
        "winsor_lower_fixed_value": "winsor_lower_fixed_value",
        "winsor_lower_percentile": "winsor_lower_percentile",
        "winsor_upper_fixed_value": "winsor_upper_fixed_value",
        "winsor_upper_percentile": "winsor_upper_percentile",
        "winsorization_strategy": "winsorization_strategy",
    }

    def __init__(
        self_,
        aging_threshold_days: Union[int, UnsetType] = unset,
        datadog_metric_measure: Union[
            ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure, UnsetType
        ] = unset,
        enable_aging_subject_filter: Union[bool, UnsetType] = unset,
        operation: Union[str, UnsetType] = unset,
        pipeline_column_suffix: Union[str, UnsetType] = unset,
        property_filters: Union[List[List[ExperimentsMetricPropertyFilter]], UnsetType] = unset,
        threshold_aggregation_type: Union[str, UnsetType] = unset,
        threshold_breach_value: Union[float, UnsetType] = unset,
        threshold_comparison_operator: Union[str, UnsetType] = unset,
        threshold_timeframe_dimension: Union[str, UnsetType] = unset,
        threshold_timeframe_value: Union[float, UnsetType] = unset,
        timeframe_end_value: Union[float, UnsetType] = unset,
        timeframe_start_value: Union[float, UnsetType] = unset,
        timeframe_unit: Union[str, UnsetType] = unset,
        warehouse_metric_measure: Union[
            ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure, UnsetType
        ] = unset,
        winsor_lower_fixed_value: Union[float, UnsetType] = unset,
        winsor_lower_percentile: Union[float, UnsetType] = unset,
        winsor_upper_fixed_value: Union[float, UnsetType] = unset,
        winsor_upper_percentile: Union[float, UnsetType] = unset,
        winsorization_strategy: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Source measure and aggregation settings for a metric value.

        :param aging_threshold_days: Stored aging threshold in days. The subject aging filter uses the aggregation window end and unit.
        :type aging_threshold_days: int, optional

        :param datadog_metric_measure: Datadog source and query that supply values for the metric.
        :type datadog_metric_measure: ExperimentsMetricV2DTODataAttributesPercentileAggregationDatadogMetricMeasure, optional

        :param enable_aging_subject_filter: Whether to exclude subjects whose observation time is shorter than the aggregation window.
        :type enable_aging_subject_filter: bool, optional

        :param operation: Aggregation applied to the selected measure.
        :type operation: str, optional

        :param pipeline_column_suffix: Suffix used to identify this value in pipeline output columns.
        :type pipeline_column_suffix: str, optional

        :param property_filters: Filters applied to the metric aggregation.
        :type property_filters: [[ExperimentsMetricPropertyFilter]], optional

        :param threshold_aggregation_type: Aggregation used to evaluate the threshold.
        :type threshold_aggregation_type: str, optional

        :param threshold_breach_value: Value used to determine whether the threshold is breached.
        :type threshold_breach_value: float, optional

        :param threshold_comparison_operator: Comparison applied between the aggregated value and the threshold.
        :type threshold_comparison_operator: str, optional

        :param threshold_timeframe_dimension: Time unit used for the threshold evaluation window.
        :type threshold_timeframe_dimension: str, optional

        :param threshold_timeframe_value: Size of the threshold evaluation window.
        :type threshold_timeframe_value: float, optional

        :param timeframe_end_value: End of the aggregation window in the specified time unit.
        :type timeframe_end_value: float, optional

        :param timeframe_start_value: Start of the aggregation window in the specified time unit.
        :type timeframe_start_value: float, optional

        :param timeframe_unit: Time unit used for the aggregation window.
        :type timeframe_unit: str, optional

        :param warehouse_metric_measure: Warehouse measure that supplies values for the metric.
        :type warehouse_metric_measure: ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure, optional

        :param winsor_lower_fixed_value: Fixed lower bound used to cap metric values.
        :type winsor_lower_fixed_value: float, optional

        :param winsor_lower_percentile: Percentile used to determine the lower bound for capped metric values.
        :type winsor_lower_percentile: float, optional

        :param winsor_upper_fixed_value: Fixed upper bound used to cap metric values.
        :type winsor_upper_fixed_value: float, optional

        :param winsor_upper_percentile: Percentile used to determine the upper bound for capped metric values.
        :type winsor_upper_percentile: float, optional

        :param winsorization_strategy: Method used to cap extreme metric values.
        :type winsorization_strategy: str, optional
        """
        if aging_threshold_days is not unset:
            kwargs["aging_threshold_days"] = aging_threshold_days
        if datadog_metric_measure is not unset:
            kwargs["datadog_metric_measure"] = datadog_metric_measure
        if enable_aging_subject_filter is not unset:
            kwargs["enable_aging_subject_filter"] = enable_aging_subject_filter
        if operation is not unset:
            kwargs["operation"] = operation
        if pipeline_column_suffix is not unset:
            kwargs["pipeline_column_suffix"] = pipeline_column_suffix
        if property_filters is not unset:
            kwargs["property_filters"] = property_filters
        if threshold_aggregation_type is not unset:
            kwargs["threshold_aggregation_type"] = threshold_aggregation_type
        if threshold_breach_value is not unset:
            kwargs["threshold_breach_value"] = threshold_breach_value
        if threshold_comparison_operator is not unset:
            kwargs["threshold_comparison_operator"] = threshold_comparison_operator
        if threshold_timeframe_dimension is not unset:
            kwargs["threshold_timeframe_dimension"] = threshold_timeframe_dimension
        if threshold_timeframe_value is not unset:
            kwargs["threshold_timeframe_value"] = threshold_timeframe_value
        if timeframe_end_value is not unset:
            kwargs["timeframe_end_value"] = timeframe_end_value
        if timeframe_start_value is not unset:
            kwargs["timeframe_start_value"] = timeframe_start_value
        if timeframe_unit is not unset:
            kwargs["timeframe_unit"] = timeframe_unit
        if warehouse_metric_measure is not unset:
            kwargs["warehouse_metric_measure"] = warehouse_metric_measure
        if winsor_lower_fixed_value is not unset:
            kwargs["winsor_lower_fixed_value"] = winsor_lower_fixed_value
        if winsor_lower_percentile is not unset:
            kwargs["winsor_lower_percentile"] = winsor_lower_percentile
        if winsor_upper_fixed_value is not unset:
            kwargs["winsor_upper_fixed_value"] = winsor_upper_fixed_value
        if winsor_upper_percentile is not unset:
            kwargs["winsor_upper_percentile"] = winsor_upper_percentile
        if winsorization_strategy is not unset:
            kwargs["winsorization_strategy"] = winsorization_strategy
        super().__init__(kwargs)
