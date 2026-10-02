# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation(ModelComposed):
    def __init__(self, **kwargs):
        """
        Measure and calculation settings for a numerator or denominator aggregation. Supply exactly one non-null measure.

        :param aging_threshold_days: Stored aging threshold in days. The subject aging filter uses the aggregation window end and unit.
        :type aging_threshold_days: int, optional

        :param datadog_metric_measure: Optional Datadog measure. Use null when the other measure is selected.
        :type datadog_metric_measure: ExperimentsNullableDatadogMetricMeasureInput, none_type, optional

        :param enable_aging_subject_filter: Whether to exclude subjects whose observation time is shorter than the aggregation window.
        :type enable_aging_subject_filter: bool, optional

        :param operation: Calculation applied to the measure values, such as sum.
        :type operation: str

        :param property_filters: Property filters that select data for this aggregation.
        :type property_filters: [[ExperimentsWarehouseFilterInput]], none_type, optional

        :param threshold_aggregation_type: Calculation used to evaluate the threshold.
        :type threshold_aggregation_type: str, optional

        :param threshold_breach_value: Value used to determine whether the threshold is breached.
        :type threshold_breach_value: float, optional

        :param threshold_comparison_operator: Operator used to compare the calculated value with the threshold.
        :type threshold_comparison_operator: str, optional

        :param threshold_timeframe_dimension: Time unit for the threshold evaluation window. Supports seconds, minutes, hours, days, calendar_days, and
            weeks. Calendar days start at midnight on the assignment day. Other units start at the assignment time.
        :type threshold_timeframe_dimension: str, optional

        :param threshold_timeframe_value: End of the threshold evaluation window, measured from assignment in the configured time unit.
        :type threshold_timeframe_value: float, optional

        :param timeframe_end_value: End offset of the aggregation window from assignment, in timeframe_unit.
        :type timeframe_end_value: float, optional

        :param timeframe_start_value: Start offset of the aggregation window from assignment, in timeframe_unit.
        :type timeframe_start_value: float, optional

        :param timeframe_unit: Time unit for the aggregation window. Calendar days are measured from midnight on the assignment day.
            Other units are measured from the assignment time.
        :type timeframe_unit: str, optional

        :param warehouse_metric_measure: Reference to a measure defined in a warehouse metric SQL model.
        :type warehouse_metric_measure: ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregationWarehouseMetricMeasure

        :param winsor_lower_fixed_value: Fixed lower bound used to cap extreme measure values.
        :type winsor_lower_fixed_value: float, optional

        :param winsor_lower_percentile: Percentile used to determine the lower bound for extreme measure values.
        :type winsor_lower_percentile: float, optional

        :param winsor_upper_fixed_value: Fixed upper bound used to cap extreme measure values.
        :type winsor_upper_fixed_value: float, optional

        :param winsor_upper_percentile: Percentile used to determine the upper bound for extreme measure values.
        :type winsor_upper_percentile: float, optional

        :param winsorization_strategy: Method used to cap extreme measure values before aggregation.
        :type winsorization_strategy: str, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.experiments_warehouse_metric_aggregation_input import (
            ExperimentsWarehouseMetricAggregationInput,
        )
        from datadog_api_client.v2.model.experiments_datadog_metric_aggregation_input import (
            ExperimentsDatadogMetricAggregationInput,
        )

        return {
            "oneOf": [
                ExperimentsWarehouseMetricAggregationInput,
                ExperimentsDatadogMetricAggregationInput,
            ],
        }
