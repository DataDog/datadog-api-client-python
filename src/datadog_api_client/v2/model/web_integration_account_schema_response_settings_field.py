# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

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


class WebIntegrationAccountSchemaResponseSettingsField(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "additional_properties": (bool,),
            "default": (
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
            "items": (dict,),
            "min_length": (int,),
            "type": (str,),
        }

    attribute_map = {
        "additional_properties": "additionalProperties",
        "default": "default",
        "description": "description",
        "items": "items",
        "min_length": "minLength",
        "type": "type",
    }

    def __init__(
        self_,
        additional_properties: Union[bool, UnsetType] = unset,
        default: Union[Any, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        items: Union[dict, UnsetType] = unset,
        min_length: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON Schema definition for a single field within settings or secrets.
        The exact fields vary by integration.

        :param additional_properties: Whether additional properties are allowed for this field.
        :type additional_properties: bool, optional

        :param default: Default value for the field if not provided.
        :type default: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param description: Human-readable description of the field's purpose.
        :type description: str, optional

        :param items: Schema for array items when type is "array".
        :type items: dict, optional

        :param min_length: Minimum length for string fields.
        :type min_length: int, optional

        :param type: The data type of the field (string, boolean, integer, array, object).
        :type type: str, optional
        """
        if additional_properties is not unset:
            kwargs["additional_properties"] = additional_properties
        if default is not unset:
            kwargs["default"] = default
        if description is not unset:
            kwargs["description"] = description
        if items is not unset:
            kwargs["items"] = items
        if min_length is not unset:
            kwargs["min_length"] = min_length
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
