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
    from datadog_api_client.v2.model.severity_override_clear_action_type import SeverityOverrideClearActionType


class SeverityOverrideClear(ModelNormal):
    validations = {
        "description": {
            "max_length": 280,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_override_clear_action_type import SeverityOverrideClearActionType

        return {
            "action": (SeverityOverrideClearActionType,),
            "description": (str,),
        }

    attribute_map = {
        "action": "action",
        "description": "description",
    }

    def __init__(self_, action: SeverityOverrideClearActionType, description: Union[str, UnsetType] = unset, **kwargs):
        """
        Removes the manual severity override of the findings.
        This action does not remove a severity set by an automation rule.

        :param action: The action that removes a manual severity override.
        :type action: SeverityOverrideClearActionType

        :param description: Additional information about the severity change. This field has a limit of 280 characters.
        :type description: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.action = action
