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
    from datadog_api_client.v2.model.automation_rule_action import AutomationRuleAction
    from datadog_api_client.v2.model.case_automation_rule_state import CaseAutomationRuleState
    from datadog_api_client.v2.model.automation_rule_trigger import AutomationRuleTrigger


class AutomationRuleCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_action import AutomationRuleAction
        from datadog_api_client.v2.model.case_automation_rule_state import CaseAutomationRuleState
        from datadog_api_client.v2.model.automation_rule_trigger import AutomationRuleTrigger

        return {
            "action": (AutomationRuleAction,),
            "name": (str,),
            "state": (CaseAutomationRuleState,),
            "trigger": (AutomationRuleTrigger,),
        }

    attribute_map = {
        "action": "action",
        "name": "name",
        "state": "state",
        "trigger": "trigger",
    }

    def __init__(
        self_,
        action: AutomationRuleAction,
        name: str,
        trigger: AutomationRuleTrigger,
        state: Union[CaseAutomationRuleState, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes required to create an automation rule.

        :param action: Defines what happens when the rule triggers. Combines an action type with action-specific configuration data.
        :type action: AutomationRuleAction

        :param name: Name of the automation rule.
        :type name: str

        :param state: Whether the automation rule is active. Enabled rules trigger on matching case events; disabled rules are inactive but preserve their configuration.
        :type state: CaseAutomationRuleState, optional

        :param trigger: Defines when the rule activates. Combines a trigger type (the case event to listen for) with optional trigger data (conditions that narrow when the trigger fires).
        :type trigger: AutomationRuleTrigger
        """
        if state is not unset:
            kwargs["state"] = state
        super().__init__(kwargs)

        self_.action = action
        self_.name = name
        self_.trigger = trigger
