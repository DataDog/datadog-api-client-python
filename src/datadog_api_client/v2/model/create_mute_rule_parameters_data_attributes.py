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
    from datadog_api_client.v2.model.action_mute import ActionMute
    from datadog_api_client.v2.model.automation_rule import AutomationRule


class CreateMuteRuleParametersDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_mute import ActionMute
        from datadog_api_client.v2.model.automation_rule import AutomationRule

        return {
            "action": (ActionMute,),
            "enabled": (bool,),
            "name": (str,),
            "rule": (AutomationRule,),
        }

    attribute_map = {
        "action": "action",
        "enabled": "enabled",
        "name": "name",
        "rule": "rule",
    }

    def __init__(
        self_, action: ActionMute, name: str, rule: AutomationRule, enabled: Union[bool, UnsetType] = unset, **kwargs
    ):
        """
        Attributes of the mute rule create request: the rule name, the rule details, the associated action, and the optional enabled field.

        :param action: Action of the mute rule
        :type action: ActionMute

        :param enabled: Field used to enable or disable the rule.
        :type enabled: bool, optional

        :param name: Name of the pipeline rule
        :type name: str

        :param rule: The definition of an automation pipeline rule scope.
            A rule can act on specific issue types, security rule types, security rule IDs, rule severities, or a query.
            The query can be used to filter resources on tags and attributes.
            The issue type and rule types fields are required.
        :type rule: AutomationRule
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)

        self_.action = action
        self_.name = name
        self_.rule = rule
