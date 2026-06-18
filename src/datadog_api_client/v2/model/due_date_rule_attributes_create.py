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
    from datadog_api_client.v2.model.due_date_rule_action import DueDateRuleAction
    from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope


class DueDateRuleAttributesCreate(ModelNormal):
    validations = {
        "name": {
            "max_length": 255,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.due_date_rule_action import DueDateRuleAction
        from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope

        return {
            "action": (DueDateRuleAction,),
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
        action: DueDateRuleAction,
        name: str,
        rule: AutomationRuleScope,
        enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a due date rule.

        :param action: The action to take when the due date rule matches a finding.
        :type action: DueDateRuleAction

        :param enabled: Whether the due date rule is enabled.
        :type enabled: bool, optional

        :param name: The name of the due date rule.
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
