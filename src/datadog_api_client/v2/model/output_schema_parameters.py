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
    from datadog_api_client.v2.model.output_schema_parameters_type import OutputSchemaParametersType


class OutputSchemaParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.output_schema_parameters_type import OutputSchemaParametersType

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
            "type": (OutputSchemaParametersType,),
            "value": (
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
        }

    attribute_map = {
        "default_value": "defaultValue",
        "description": "description",
        "label": "label",
        "name": "name",
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        name: str,
        type: OutputSchemaParametersType,
        default_value: Union[Any, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        label: Union[str, UnsetType] = unset,
        value: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``OutputSchemaParameters`` object.

        :param default_value: The ``OutputSchemaParameters`` ``defaultValue``.
        :type default_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param description: The ``OutputSchemaParameters`` ``description``.
        :type description: str, optional

        :param label: The ``OutputSchemaParameters`` ``label``.
        :type label: str, optional

        :param name: The ``OutputSchemaParameters`` ``name``.
        :type name: str

        :param type: The definition of ``OutputSchemaParametersType`` object.
        :type type: OutputSchemaParametersType

        :param value: The ``OutputSchemaParameters`` ``value``.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if default_value is not unset:
            kwargs["default_value"] = default_value
        if description is not unset:
            kwargs["description"] = description
        if label is not unset:
            kwargs["label"] = label
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
