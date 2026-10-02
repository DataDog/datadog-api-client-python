# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point_filters_items_items_column_type import (
        ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
    )


class ExperimentsCreateExperimentV2RequestDataAttributesSplitByPropertiesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point_filters_items_items_column_type import (
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
        )

        return {
            "column_name": (str,),
            "column_type": (
                ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
            ),
            "name": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "name": "name",
    }

    def __init__(
        self_,
        column_name: str,
        column_type: Union[
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
            UnsetType,
        ] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Complete Datadog split-by selection. Identify each property by column_name. Omit this field to copy organization defaults.

        :param column_name: Exposure field that identifies the property.
        :type column_name: str

        :param column_type: Data type of the column evaluated by the entry-point filter.
        :type column_type: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType, optional

        :param name: Optional display name. Defaults to column_name for a new property.
        :type name: str, optional
        """
        if column_type is not unset:
            kwargs["column_type"] = column_type
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.column_name = column_name
