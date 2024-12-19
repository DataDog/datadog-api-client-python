# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.input_schema_data_attributes_parameters_items import (
        InputSchemaDataAttributesParametersItems,
    )


class InputSchemaDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.input_schema_data_attributes_parameters_items import (
            InputSchemaDataAttributesParametersItems,
        )

        return {
            "parameters": ([InputSchemaDataAttributesParametersItems],),
        }

    attribute_map = {
        "parameters": "parameters",
    }

    def __init__(self_, parameters: Union[List[InputSchemaDataAttributesParametersItems], UnsetType] = unset, **kwargs):
        """
        The definition of ``InputSchemaDataAttributes`` object.

        :param parameters: The ``attributes`` ``parameters``.
        :type parameters: [InputSchemaDataAttributesParametersItems], optional
        """
        if parameters is not unset:
            kwargs["parameters"] = parameters
        super().__init__(kwargs)
