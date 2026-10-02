# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation(ModelComposed):
    def __init__(self, **kwargs):
        """
        Measure and percentile to calculate for the metric. Supply exactly one non-null measure.

        :param datadog_metric_measure: Optional Datadog percentile measure. Use null when the warehouse measure is selected.
        :type datadog_metric_measure: ExperimentsNullableDatadogPercentileMeasureInput, none_type, optional

        :param percentile: Percentile to calculate from the measure values.
        :type percentile: float

        :param property_filters: Property filters that select data for the percentile calculation.
        :type property_filters: [[ExperimentsPropertyFilterInput]], none_type, optional

        :param warehouse_metric_measure: Reference to a measure defined in a warehouse metric SQL model.
        :type warehouse_metric_measure: ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregationWarehouseMetricMeasure
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
        from datadog_api_client.v2.model.experiments_warehouse_percentile_aggregation_input import (
            ExperimentsWarehousePercentileAggregationInput,
        )
        from datadog_api_client.v2.model.experiments_datadog_percentile_aggregation_input import (
            ExperimentsDatadogPercentileAggregationInput,
        )

        return {
            "oneOf": [
                ExperimentsWarehousePercentileAggregationInput,
                ExperimentsDatadogPercentileAggregationInput,
            ],
        }
