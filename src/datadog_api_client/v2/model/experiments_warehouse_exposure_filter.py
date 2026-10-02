# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration_entry_point_filters_items_operation import (
        ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
    )


class ExperimentsWarehouseExposureFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration_entry_point_filters_items_operation import (
            ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
        )

        return {
            "operation": (
                ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
            ),
            "property_id": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "operation": "operation",
        "property_id": "property_id",
        "values": "values",
    }

    def __init__(
        self_,
        operation: ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation,
        property_id: str,
        values: List[str],
        **kwargs,
    ):
        """
        A comparison that selects warehouse exposure data by a property.

        :param operation: Comparison applied by the warehouse entry-point filter.
        :type operation: ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation

        :param property_id: Warehouse property UUID.
        :type property_id: str

        :param values: Ordered values used by the filter.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.operation = operation
        self_.property_id = property_id
        self_.values = values
