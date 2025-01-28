# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.inbox_rule_attributes import InboxRuleAttributes
    from datadog_api_client.v2.model.inbox_rules_type import InboxRulesType


class InboxRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.inbox_rule_attributes import InboxRuleAttributes
        from datadog_api_client.v2.model.inbox_rules_type import InboxRulesType

        return {
            "attributes": (InboxRuleAttributes,),
            "id": (UUID,),
            "type": (InboxRulesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: InboxRuleAttributes, id: UUID, type: InboxRulesType, **kwargs):
        """
        Inbox rules are used to prioritize and add relevant vulnerabilities to your Security Inbox.
        An inbox rule is composed of a rule UUID, a rule type, and the rule attributes. All fields are required.

        :param attributes: Attributes of the inbox rule
        :type attributes: InboxRuleAttributes

        :param id: The ID of a pipeline rule
        :type id: UUID

        :param type: The pipeline rule type associated to inbox rules
        :type type: InboxRulesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
