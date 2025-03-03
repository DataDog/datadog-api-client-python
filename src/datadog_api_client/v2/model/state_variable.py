# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.state_variable_properties import StateVariableProperties
    from datadog_api_client.v2.model.state_variable_type import StateVariableType


class StateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.state_variable_properties import StateVariableProperties
        from datadog_api_client.v2.model.state_variable_type import StateVariableType

        return {
            "id": (UUID,),
            "name": (str,),
            "properties": (StateVariableProperties,),
            "type": (StateVariableType,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "properties": "properties",
        "type": "type",
    }

    def __init__(self_, id: UUID, name: str, properties: StateVariableProperties, type: StateVariableType, **kwargs):
        """
        A variable, which can be set and read by other components in the app.

        :param id: The ID of the state variable.
        :type id: UUID

        :param name: A unique identifier for this state variable. This name is also used to access the variable's value throughout the app.
        :type name: str

        :param properties: The properties of the state variable.
        :type properties: StateVariableProperties

        :param type: The state variable type.
        :type type: StateVariableType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.properties = properties
        self_.type = type
