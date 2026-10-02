# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_split_by_properties_items_column_type import (
        ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType,
    )


class ExperimentsExperimentV2DTODataAttributesSplitByPropertiesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_response_data_attributes_split_by_properties_items_column_type import (
            ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType,
        )

        return {
            "column_name": (str,),
            "column_type": (ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType,),
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "id": "id",
        "name": "name",
    }

    def __init__(
        self_,
        column_name: str,
        column_type: ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType,
        id: str,
        name: str,
        **kwargs,
    ):
        """
        Property used to split experiment results into analysis dimensions.

        :param column_name: Exposure field or Warehouse column used for the analysis dimension.
        :type column_name: str

        :param column_type: Type of the Datadog exposure field or Warehouse column.
        :type column_type: ExperimentsPatchExperimentV2ResponseDataAttributesSplitByPropertiesItemsColumnType

        :param id: Read-only property ID. Omit it from POST and PATCH; writes identify properties by column_name.
        :type id: str

        :param name: Display name for the analysis dimension.
        :type name: str
        """
        super().__init__(kwargs)

        self_.column_name = column_name
        self_.column_type = column_type
        self_.id = id
        self_.name = name
