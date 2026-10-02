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
    from datadog_api_client.v2.model.experiments_nullable_datadog_percentile_measure_input import (
        ExperimentsNullableDatadogPercentileMeasureInput,
    )
    from datadog_api_client.v2.model.experiments_property_filter_input import ExperimentsPropertyFilterInput
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_percentile_aggregation_warehouse_metric_measure import (
        ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregationWarehouseMetricMeasure,
    )


class ExperimentsWarehousePercentileAggregationInput(ModelNormal):
    validations = {
        "percentile": {
            "exclusive_maximum": 1,
            "exclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_nullable_datadog_percentile_measure_input import (
            ExperimentsNullableDatadogPercentileMeasureInput,
        )
        from datadog_api_client.v2.model.experiments_property_filter_input import ExperimentsPropertyFilterInput
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_percentile_aggregation_warehouse_metric_measure import (
            ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregationWarehouseMetricMeasure,
        )

        return {
            "datadog_metric_measure": (ExperimentsNullableDatadogPercentileMeasureInput,),
            "percentile": (float,),
            "property_filters": ([[ExperimentsPropertyFilterInput]], none_type),
            "warehouse_metric_measure": (
                ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregationWarehouseMetricMeasure,
            ),
        }

    attribute_map = {
        "datadog_metric_measure": "datadog_metric_measure",
        "percentile": "percentile",
        "property_filters": "property_filters",
        "warehouse_metric_measure": "warehouse_metric_measure",
    }

    def __init__(
        self_,
        percentile: float,
        warehouse_metric_measure: ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregationWarehouseMetricMeasure,
        datadog_metric_measure: Union[ExperimentsNullableDatadogPercentileMeasureInput, none_type, UnsetType] = unset,
        property_filters: Union[List[List[ExperimentsPropertyFilterInput]], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for a percentile aggregation that uses a Warehouse measure. The other measure must be omitted or null.

        :param datadog_metric_measure: Optional Datadog percentile measure. Use null when the warehouse measure is selected.
        :type datadog_metric_measure: ExperimentsNullableDatadogPercentileMeasureInput, none_type, optional

        :param percentile: Percentile to calculate from the measure values.
        :type percentile: float

        :param property_filters: Property filters that select data for the percentile calculation.
        :type property_filters: [[ExperimentsPropertyFilterInput]], none_type, optional

        :param warehouse_metric_measure: Reference to a measure defined in a warehouse metric SQL model.
        :type warehouse_metric_measure: ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregationWarehouseMetricMeasure
        """
        if datadog_metric_measure is not unset:
            kwargs["datadog_metric_measure"] = datadog_metric_measure
        if property_filters is not unset:
            kwargs["property_filters"] = property_filters
        super().__init__(kwargs)

        self_.percentile = percentile
        self_.warehouse_metric_measure = warehouse_metric_measure
