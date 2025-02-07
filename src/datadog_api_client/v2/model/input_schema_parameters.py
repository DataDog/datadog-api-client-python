# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.input_schema_parameters_type import InputSchemaParametersType


class InputSchemaParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.input_schema_parameters_type import InputSchemaParametersType

        return {
            "default_value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "description": (str,),
            "label": (str,),
            "name": (str,),
            "type": (InputSchemaParametersType,),
        }

    attribute_map = {
        "default_value": "defaultValue",
        "description": "description",
        "label": "label",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        type: InputSchemaParametersType,
        default_value: Union[Any, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``InputSchemaParameters`` object.

        :param default_value: The ``InputSchemaParameters`` ``defaultValue``.
        :type default_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param description: The ``InputSchemaParameters`` ``description``.
        :type description: str, optional

        :param label: The ``InputSchemaParameters`` ``label``.
        :type label: str, optional

        :param name: The ``InputSchemaParameters`` ``name``.
        :type name: str

        :param type: The definition of ``InputSchemaParametersType`` object.
        :type type: InputSchemaParametersType
        """
        if default_value is not unset:
            kwargs["default_value"] = default_value
        if description is not unset:
            kwargs["description"] = description
        if label is not unset:
            kwargs["label"] = label
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
