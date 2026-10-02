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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration_entry_point_filters_items_operation import (
        ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
    )


class ExperimentsPropertyFilterInput(ModelNormal):
    validations = {
        "measure_id": {},
        "property_id": {
            "min_length": 1,
        },
        "values": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration_entry_point_filters_items_operation import (
            ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
        )

        return {
            "measure_id": (str, none_type),
            "operation": (
                ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
            ),
            "property_id": (UUID,),
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
        operation: ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
        property_id: UUID,
        values: List[str],
        measure_id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A property comparison for metric source data.

        :param measure_id: Omit this target or use null or a blank string.
        :type measure_id: str, none_type, optional

        :param operation: Comparison applied by the warehouse entry-point filter.
        :type operation: ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation

        :param property_id: ID of the property on the aggregation source.
        :type property_id: UUID

        :param values: Values used by the comparison.
        :type values: [str]
        """
        if measure_id is not unset:
            kwargs["measure_id"] = measure_id
        super().__init__(kwargs)

        self_.operation = operation
        self_.property_id = property_id
        self_.values = values
