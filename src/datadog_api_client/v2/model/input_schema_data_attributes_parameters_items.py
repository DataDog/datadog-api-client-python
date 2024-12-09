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
    from datadog_api_client.v2.model.input_schema_data_attributes_parameters_items_data import (
        InputSchemaDataAttributesParametersItemsData,
    )


class InputSchemaDataAttributesParametersItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.input_schema_data_attributes_parameters_items_data import (
            InputSchemaDataAttributesParametersItemsData,
        )

        return {
            "data": (InputSchemaDataAttributesParametersItemsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[InputSchemaDataAttributesParametersItemsData, UnsetType] = unset, **kwargs):
        """
        The definition of ``InputSchemaDataAttributesParametersItems`` object.

        :param data: The definition of ``InputSchemaDataAttributesParametersItemsData`` object.
        :type data: InputSchemaDataAttributesParametersItemsData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
