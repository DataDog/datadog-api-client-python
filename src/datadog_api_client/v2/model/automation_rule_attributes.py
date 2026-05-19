# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.automation_rule_action import AutomationRuleAction
    from datadog_api_client.v2.model.case_automation_rule_state import CaseAutomationRuleState
    from datadog_api_client.v2.model.automation_rule_trigger import AutomationRuleTrigger


class AutomationRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_action import AutomationRuleAction
        from datadog_api_client.v2.model.case_automation_rule_state import CaseAutomationRuleState
        from datadog_api_client.v2.model.automation_rule_trigger import AutomationRuleTrigger

        return {
            "action": (AutomationRuleAction,),
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "name": (str,),
            "state": (CaseAutomationRuleState,),
            "trigger": (AutomationRuleTrigger,),
        }

    attribute_map = {
        "action": "action",
        "created_at": "created_at",
        "modified_at": "modified_at",
        "name": "name",
        "state": "state",
        "trigger": "trigger",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        action: AutomationRuleAction,
        created_at: datetime,
        name: str,
        state: CaseAutomationRuleState,
        trigger: AutomationRuleTrigger,
        modified_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Core attributes of an automation rule, including its name, trigger condition, action to execute, and current state.

        :param action: Defines what happens when the rule triggers. Combines an action type with action-specific configuration data.
        :type action: AutomationRuleAction

        :param created_at: Timestamp when the automation rule was created.
        :type created_at: datetime

        :param modified_at: Timestamp when the automation rule was last modified.
        :type modified_at: datetime, optional

        :param name: A human-readable name for the automation rule, used to identify the rule in the UI and API responses.
        :type name: str

        :param state: Whether the automation rule is active. Enabled rules trigger on matching case events; disabled rules are inactive but preserve their configuration.
        :type state: CaseAutomationRuleState

        :param trigger: Defines when the rule activates. Combines a trigger type (the case event to listen for) with optional trigger data (conditions that narrow when the trigger fires).
        :type trigger: AutomationRuleTrigger
        """
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        super().__init__(kwargs)

        self_.action = action
        self_.created_at = created_at
        self_.name = name
        self_.state = state
        self_.trigger = trigger
