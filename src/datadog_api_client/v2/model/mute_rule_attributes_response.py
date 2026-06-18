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
    from datadog_api_client.v2.model.mute_rule_action import MuteRuleAction
    from datadog_api_client.v2.model.automation_rule_created_by import AutomationRuleCreatedBy
    from datadog_api_client.v2.model.automation_rule_modified_by import AutomationRuleModifiedBy
    from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope


class MuteRuleAttributesResponse(ModelNormal):
    validations = {
        "name": {
            "max_length": 255,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_rule_action import MuteRuleAction
        from datadog_api_client.v2.model.automation_rule_created_by import AutomationRuleCreatedBy
        from datadog_api_client.v2.model.automation_rule_modified_by import AutomationRuleModifiedBy
        from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope

        return {
            "action": (MuteRuleAction,),
            "created_at": (int,),
            "created_by": (AutomationRuleCreatedBy,),
            "enabled": (bool,),
            "modified_at": (int,),
            "modified_by": (AutomationRuleModifiedBy,),
            "name": (str,),
            "rule": (AutomationRuleScope,),
        }

    attribute_map = {
        "action": "action",
        "created_at": "created_at",
        "created_by": "created_by",
        "enabled": "enabled",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "rule": "rule",
    }

    def __init__(
        self_,
        action: MuteRuleAction,
        created_at: int,
        created_by: AutomationRuleCreatedBy,
        enabled: bool,
        modified_at: int,
        modified_by: AutomationRuleModifiedBy,
        name: str,
        rule: AutomationRuleScope,
        **kwargs,
    ):
        """
        Attributes of a mute rule returned by the API.

        :param action: The action to take when the mute rule matches a finding.
        :type action: MuteRuleAction

        :param created_at: The Unix timestamp in milliseconds when the rule was created.
        :type created_at: int

        :param created_by: The user or Datadog system who created the rule.
        :type created_by: AutomationRuleCreatedBy

        :param enabled: Whether the mute rule is enabled.
        :type enabled: bool

        :param modified_at: The Unix timestamp in milliseconds when the rule was last modified.
        :type modified_at: int

        :param modified_by: The user or Datadog system who last modified the rule.
        :type modified_by: AutomationRuleModifiedBy

        :param name: The name of the mute rule.
        :type name: str

        :param rule: Defines the scope of findings to which the automation rule applies.
        :type rule: AutomationRuleScope
        """
        super().__init__(kwargs)

        self_.action = action
        self_.created_at = created_at
        self_.created_by = created_by
        self_.enabled = enabled
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.name = name
        self_.rule = rule
