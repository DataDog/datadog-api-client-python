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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point_filters_items_items_column_type import (
        ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
    )
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point_filters_items_items_operation import (
        ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsOperation,
    )


class ExperimentsDatadogEntryPointFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point_filters_items_items_column_type import (
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
        )
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_datadog_flag_configuration_entry_point_filters_items_items_operation import (
            ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsOperation,
        )

        return {
            "column": (str,),
            "column_type": (
                ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
            ),
            "operation": (
                ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsOperation,
            ),
            "values": ([str],),
        }

    attribute_map = {
        "column": "column",
        "column_type": "column_type",
        "operation": "operation",
        "values": "values",
    }

    def __init__(
        self_,
        column: str,
        column_type: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType,
        operation: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsOperation,
        values: List[str],
        **kwargs,
    ):
        """
        Complete Datadog OR-of-ANDs entry-point filter expression.

        :param column: Exposure field evaluated by the entry-point filter.
        :type column: str

        :param column_type: Data type of the column evaluated by the entry-point filter.
        :type column_type: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsColumnType

        :param operation: Comparison applied by the Datadog entry-point filter.
        :type operation: ExperimentsPatchExperimentV2ResponseDataAttributesDatadogFlagConfigurationEntryPointFiltersItemsItemsOperation

        :param values: Comparison values used by the filter operation.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.column = column
        self_.column_type = column_type
        self_.operation = operation
        self_.values = values
