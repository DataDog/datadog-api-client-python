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
    from datadog_api_client.v2.model.input_schema_data_attributes_parameters_items_data_attributes import (
        InputSchemaDataAttributesParametersItemsDataAttributes,
    )


class InputSchemaDataAttributesParametersItemsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.input_schema_data_attributes_parameters_items_data_attributes import (
            InputSchemaDataAttributesParametersItemsDataAttributes,
        )

        return {
            "attributes": (InputSchemaDataAttributesParametersItemsDataAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(
        self_, attributes: Union[InputSchemaDataAttributesParametersItemsDataAttributes, UnsetType] = unset, **kwargs
    ):
        """
        The definition of ``InputSchemaDataAttributesParametersItemsData`` object.

        :param attributes: The definition of ``InputSchemaDataAttributesParametersItemsDataAttributes`` object.
        :type attributes: InputSchemaDataAttributesParametersItemsDataAttributes, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)
