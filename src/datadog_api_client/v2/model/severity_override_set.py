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
    from datadog_api_client.v2.model.severity_override_set_action_type import SeverityOverrideSetActionType
    from datadog_api_client.v2.model.severity_override_value import SeverityOverrideValue


class SeverityOverrideSet(ModelNormal):
    validations = {
        "description": {
            "max_length": 280,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_override_set_action_type import SeverityOverrideSetActionType
        from datadog_api_client.v2.model.severity_override_value import SeverityOverrideValue

        return {
            "action": (SeverityOverrideSetActionType,),
            "description": (str,),
            "value": (SeverityOverrideValue,),
        }

    attribute_map = {
        "action": "action",
        "description": "description",
        "value": "value",
    }

    def __init__(
        self_,
        action: SeverityOverrideSetActionType,
        value: SeverityOverrideValue,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Applies a manual severity override to the findings.

        :param action: The action that applies a manual severity override.
        :type action: SeverityOverrideSetActionType

        :param description: Additional information about the severity change. This field has a limit of 280 characters.
        :type description: str, optional

        :param value: Severity to apply to the findings.
            ``info`` sets the lowest severity the finding type allows.
        :type value: SeverityOverrideValue
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.action = action
        self_.value = value
