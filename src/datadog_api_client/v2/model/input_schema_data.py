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
    from datadog_api_client.v2.model.input_schema_data_attributes import InputSchemaDataAttributes
    from datadog_api_client.v2.model.input_schema_data_type import InputSchemaDataType


class InputSchemaData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.input_schema_data_attributes import InputSchemaDataAttributes
        from datadog_api_client.v2.model.input_schema_data_type import InputSchemaDataType

        return {
            "attributes": (InputSchemaDataAttributes,),
            "id": (str,),
            "type": (InputSchemaDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[InputSchemaDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[InputSchemaDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``InputSchemaData`` object.

        :param attributes: The definition of ``InputSchemaDataAttributes`` object.
        :type attributes: InputSchemaDataAttributes, optional

        :param id: The ``data`` ``id``.
        :type id: str, optional

        :param type: The definition of ``InputSchemaDataType`` object.
        :type type: InputSchemaDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
