# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_control_supported_value import GovernanceControlSupportedValue


class GovernanceControlParameterDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_supported_value import GovernanceControlSupportedValue

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
            "display_name": (str,),
            "hidden": (bool,),
            "name": (str,),
            "required": (bool,),
            "supported_values": ([GovernanceControlSupportedValue],),
            "type": (str,),
        }

    attribute_map = {
        "default_value": "default_value",
        "description": "description",
        "display_name": "display_name",
        "hidden": "hidden",
        "name": "name",
        "required": "required",
        "supported_values": "supported_values",
        "type": "type",
    }

    def __init__(
        self_,
        default_value: Any,
        description: str,
        display_name: str,
        hidden: bool,
        name: str,
        required: bool,
        supported_values: List[GovernanceControlSupportedValue],
        type: str,
        **kwargs,
    ):
        """
        The definition of a configurable parameter on a control or mitigation.

        :param default_value: The default value of the parameter. The JSON type depends on the parameter's ``type``.
        :type default_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param description: A human-readable description of the parameter.
        :type description: str

        :param display_name: The human-readable name of the parameter.
        :type display_name: str

        :param hidden: Whether the parameter is hidden from the UI.
        :type hidden: bool

        :param name: The machine-readable name of the parameter.
        :type name: str

        :param required: Whether the parameter must be provided.
        :type required: bool

        :param supported_values: The supported values for an enumerated parameter.
        :type supported_values: [GovernanceControlSupportedValue]

        :param type: The type of the parameter, such as ``integer`` , ``string`` , ``boolean`` , ``enum`` , or ``pattern_list``.
        :type type: str
        """
        super().__init__(kwargs)

        self_.default_value = default_value
        self_.description = description
        self_.display_name = display_name
        self_.hidden = hidden
        self_.name = name
        self_.required = required
        self_.supported_values = supported_values
        self_.type = type
