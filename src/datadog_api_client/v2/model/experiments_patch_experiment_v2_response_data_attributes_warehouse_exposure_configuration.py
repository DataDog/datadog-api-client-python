# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration_entry_point import (
        ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPoint,
    )


class ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfiguration(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_warehouse_exposure_configuration_entry_point import (
            ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPoint,
        )

        return {
            "entry_point": (
                ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPoint,
            ),
            "experiment_key": (str, none_type),
            "exposure_sql_model_id": (str,),
        }

    attribute_map = {
        "entry_point": "entry_point",
        "experiment_key": "experiment_key",
        "exposure_sql_model_id": "exposure_sql_model_id",
    }

    def __init__(
        self_,
        entry_point: Union[
            ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPoint, none_type
        ],
        experiment_key: Union[str, none_type],
        exposure_sql_model_id: str,
        **kwargs,
    ):
        """
        Warehouse exposure model and settings used to identify experiment assignments.

        :param entry_point: Optional Warehouse measure that scopes analyzed subjects.
        :type entry_point: ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPoint, none_type

        :param experiment_key: Warehouse experiment key. Reads can return null for incomplete configuration; configuration writes require a value.
        :type experiment_key: str, none_type

        :param exposure_sql_model_id: ID of the exposure SQL model that provides assignment data.
        :type exposure_sql_model_id: str
        """
        super().__init__(kwargs)

        self_.entry_point = entry_point
        self_.experiment_key = experiment_key
        self_.exposure_sql_model_id = exposure_sql_model_id
