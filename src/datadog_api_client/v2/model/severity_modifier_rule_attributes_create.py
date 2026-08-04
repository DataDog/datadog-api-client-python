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
    from datadog_api_client.v2.model.severity_modifier_rule_action import SeverityModifierRuleAction
    from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope
    from datadog_api_client.v2.model.severity_modifier_rule_set_action import SeverityModifierRuleSetAction
    from datadog_api_client.v2.model.severity_modifier_rule_shift_action import SeverityModifierRuleShiftAction


class SeverityModifierRuleAttributesCreate(ModelNormal):
    validations = {
        "name": {
            "max_length": 255,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_modifier_rule_action import SeverityModifierRuleAction
        from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope

        return {
            "action": (SeverityModifierRuleAction,),
            "enabled": (bool,),
            "name": (str,),
            "rule": (AutomationRuleScope,),
        }

    attribute_map = {
        "action": "action",
        "enabled": "enabled",
        "name": "name",
        "rule": "rule",
    }

    def __init__(
        self_,
        action: Union[SeverityModifierRuleAction, SeverityModifierRuleSetAction, SeverityModifierRuleShiftAction],
        name: str,
        rule: AutomationRuleScope,
        enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a severity modifier rule.

        :param action: The action to take when a severity modifier rule matches a finding. This is a discriminated union on ``type`` : ``set`` assigns a fixed severity, while ``shift`` moves the severity up or down by one rank.

            A severity modifier rule's ``rule.query`` must not filter on ``@severity`` or on the ``@severity_details.user_adjusted.*`` namespace.

            Use ``@severity_details.adjusted.value`` instead, which reflects the severity before user-defined adjustments.
        :type action: SeverityModifierRuleAction

        :param enabled: Whether the severity modifier rule is enabled.
        :type enabled: bool, optional

        :param name: The name of the severity modifier rule.
        :type name: str

        :param rule: Defines the scope of findings to which the automation rule applies.
        :type rule: AutomationRuleScope
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)

        self_.action = action
        self_.name = name
        self_.rule = rule
