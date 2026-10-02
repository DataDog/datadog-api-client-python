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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_measure_comparison_filter_input_operation import (
        ExperimentsMeasureComparisonFilterInputOperation,
    )


class ExperimentsMeasureComparisonFilterInput(ModelNormal):
    validations = {
        "measure_id": {
            "min_length": 1,
        },
        "property_id": {},
        "values": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_measure_comparison_filter_input_operation import (
            ExperimentsMeasureComparisonFilterInputOperation,
        )

        return {
            "measure_id": (UUID,),
            "operation": (ExperimentsMeasureComparisonFilterInputOperation,),
            "property_id": (str, none_type),
            "values": ([str],),
        }

    attribute_map = {
        "measure_id": "measure_id",
        "operation": "operation",
        "property_id": "property_id",
        "values": "values",
    }

    def __init__(
        self_,
        measure_id: UUID,
        operation: ExperimentsMeasureComparisonFilterInputOperation,
        values: List[str],
        property_id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A measure comparison for metric source data.

        :param measure_id: ID of the measure on the aggregation source.
        :type measure_id: UUID

        :param operation: Comparison applied by this filter.
        :type operation: ExperimentsMeasureComparisonFilterInputOperation

        :param property_id: Omit this target or use null or a blank string.
        :type property_id: str, none_type, optional

        :param values: Values used by the comparison.
        :type values: [str]
        """
        if property_id is not unset:
            kwargs["property_id"] = property_id
        super().__init__(kwargs)

        self_.measure_id = measure_id
        self_.operation = operation
        self_.values = values
