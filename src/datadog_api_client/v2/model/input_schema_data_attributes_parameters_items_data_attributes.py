# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union

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


class InputSchemaDataAttributesParametersItemsDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
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
            "enum": ([str],),
            "label": (str,),
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "default_value": "defaultValue",
        "description": "description",
        "enum": "enum",
        "label": "label",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        default_value: Union[Any, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        enum: Union[List[str], UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``InputSchemaDataAttributesParametersItemsDataAttributes`` object.

        :param default_value: The ``attributes`` ``defaultValue``.
        :type default_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param description: The ``attributes`` ``description``.
        :type description: str, optional

        :param enum: The ``attributes`` ``enum``.
        :type enum: [str], optional

        :param label: The ``attributes`` ``label``.
        :type label: str, optional

        :param name: The ``attributes`` ``name``.
        :type name: str, optional

        :param type: The ``attributes`` ``type``.
        :type type: str, optional
        """
        if default_value is not unset:
            kwargs["default_value"] = default_value
        if description is not unset:
            kwargs["description"] = description
        if enum is not unset:
            kwargs["enum"] = enum
        if label is not unset:
            kwargs["label"] = label
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
