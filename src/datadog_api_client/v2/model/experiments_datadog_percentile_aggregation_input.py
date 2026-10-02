# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_datadog_percentile_measure_input import (
        ExperimentsDatadogPercentileMeasureInput,
    )
    from datadog_api_client.v2.model.experiments_property_filter_input import ExperimentsPropertyFilterInput
    from datadog_api_client.v2.model.experiments_nullable_warehouse_metric_measure_input import (
        ExperimentsNullableWarehouseMetricMeasureInput,
    )


class ExperimentsDatadogPercentileAggregationInput(ModelNormal):
    validations = {
        "percentile": {
            "exclusive_maximum": 1,
            "exclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_datadog_percentile_measure_input import (
            ExperimentsDatadogPercentileMeasureInput,
        )
        from datadog_api_client.v2.model.experiments_property_filter_input import ExperimentsPropertyFilterInput
        from datadog_api_client.v2.model.experiments_nullable_warehouse_metric_measure_input import (
            ExperimentsNullableWarehouseMetricMeasureInput,
        )

        return {
            "datadog_metric_measure": (ExperimentsDatadogPercentileMeasureInput,),
            "percentile": (float,),
            "property_filters": ([[ExperimentsPropertyFilterInput]], none_type),
            "warehouse_metric_measure": (ExperimentsNullableWarehouseMetricMeasureInput,),
        }

    attribute_map = {
        "datadog_metric_measure": "datadog_metric_measure",
        "percentile": "percentile",
        "property_filters": "property_filters",
        "warehouse_metric_measure": "warehouse_metric_measure",
    }

    def __init__(
        self_,
        datadog_metric_measure: ExperimentsDatadogPercentileMeasureInput,
        percentile: float,
        property_filters: Union[List[List[ExperimentsPropertyFilterInput]], none_type, UnsetType] = unset,
        warehouse_metric_measure: Union[ExperimentsNullableWarehouseMetricMeasureInput, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for a percentile aggregation that uses a Datadog measure. The other measure must be omitted or null.

        :param datadog_metric_measure: Datadog measure used to calculate a percentile.
        :type datadog_metric_measure: ExperimentsDatadogPercentileMeasureInput

        :param percentile: Percentile to calculate from the measure values.
        :type percentile: float

        :param property_filters: Property filters that select data for the percentile calculation.
        :type property_filters: [[ExperimentsPropertyFilterInput]], none_type, optional

        :param warehouse_metric_measure: Optional warehouse measure. Use null when the other measure is selected.
        :type warehouse_metric_measure: ExperimentsNullableWarehouseMetricMeasureInput, none_type, optional
        """
        if property_filters is not unset:
            kwargs["property_filters"] = property_filters
        if warehouse_metric_measure is not unset:
            kwargs["warehouse_metric_measure"] = warehouse_metric_measure
        super().__init__(kwargs)

        self_.datadog_metric_measure = datadog_metric_measure
        self_.percentile = percentile
