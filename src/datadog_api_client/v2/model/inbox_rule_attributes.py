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
    from datadog_api_client.v2.model.action_inbox import ActionInbox
    from datadog_api_client.v2.model.rule_user import RuleUser
    from datadog_api_client.v2.model.rule import Rule


class InboxRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_inbox import ActionInbox
        from datadog_api_client.v2.model.rule_user import RuleUser
        from datadog_api_client.v2.model.rule import Rule

        return {
            "action": (ActionInbox,),
            "created_at": (int,),
            "created_by": (RuleUser,),
            "enabled": (bool,),
            "modified_at": (int,),
            "modified_by": (RuleUser,),
            "name": (str,),
            "rule": (Rule,),
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
        action: ActionInbox,
        created_at: int,
        created_by: RuleUser,
        enabled: bool,
        modified_at: int,
        modified_by: RuleUser,
        name: str,
        rule: Rule,
        **kwargs,
    ):
        """
        Attributes of the inbox rule

        :param action: Action of the inbox rule
        :type action: ActionInbox

        :param created_at: Date as Unix timestamp in milliseconds
        :type created_at: int

        :param created_by: User creating or modifying a rule
        :type created_by: RuleUser

        :param enabled: Field used to enable or disable the rule.
        :type enabled: bool

        :param modified_at: Date as Unix timestamp in milliseconds
        :type modified_at: int

        :param modified_by: User creating or modifying a rule
        :type modified_by: RuleUser

        :param name: Name of the pipeline rule
        :type name: str

        :param rule: The definition of an automation pipeline rule scope.
            A rule can act on specific issue types, security rule types, security rule IDs, rule severities, or a query.
            The query can be used to filter resources on tags and attributes.
            The issue type and rule types fields are required.
        :type rule: Rule
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
