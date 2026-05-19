# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.automation_rule_action_data import AutomationRuleActionData
    from datadog_api_client.v2.model.automation_rule_action_type import AutomationRuleActionType


class AutomationRuleAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_action_data import AutomationRuleActionData
        from datadog_api_client.v2.model.automation_rule_action_type import AutomationRuleActionType

        return {
            "data": (AutomationRuleActionData,),
            "type": (AutomationRuleActionType,),
        }

    attribute_map = {
        "data": "data",
        "type": "type",
    }

    def __init__(self_, data: AutomationRuleActionData, type: AutomationRuleActionType, **kwargs):
        """
        Defines what happens when the rule triggers. Combines an action type with action-specific configuration data.

        :param data: Configuration for the action to execute, dependent on the action type.
        :type data: AutomationRuleActionData

        :param type: The type of automated action to perform when the rule triggers. ``execute_workflow`` runs a Datadog workflow; ``assign_agent`` assigns an AI agent to the case.
        :type type: AutomationRuleActionType
        """
        super().__init__(kwargs)

        self_.data = data
        self_.type = type
