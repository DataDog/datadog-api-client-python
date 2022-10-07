# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType


class SyntheticsConfigVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType

        return {
            "example": (str,),
            "id": (str,),
            "name": (str,),
            "pattern": (str,),
            "type": (SyntheticsConfigVariableType,),
        }

    attribute_map = {
        "example": "example",
        "id": "id",
        "name": "name",
        "pattern": "pattern",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        type: SyntheticsConfigVariableType,
        example: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        pattern: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object defining a variable that can be used in your test configuration.

        :param example: Example for the variable.
        :type example: str, optional

        :param id: ID of the variable for global variables.
        :type id: str, optional

        :param name: Name of the variable.
        :type name: str

        :param pattern: Pattern of the variable.
        :type pattern: str, optional

        :param type: Type of the configuration variable.
        :type type: SyntheticsConfigVariableType
        """
        if example is not unset:
            kwargs["example"] = example
        if id is not unset:
            kwargs["id"] = id
        if pattern is not unset:
            kwargs["pattern"] = pattern
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
