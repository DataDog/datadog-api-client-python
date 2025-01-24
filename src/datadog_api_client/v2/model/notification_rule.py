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
    from datadog_api_client.v2.model.notification_rule_attributes import NotificationRuleAttributes
    from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType


class NotificationRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_rule_attributes import NotificationRuleAttributes
        from datadog_api_client.v2.model.notification_rules_type import NotificationRulesType

        return {
            "attributes": (NotificationRuleAttributes,),
            "id": (str,),
            "type": (NotificationRulesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: NotificationRuleAttributes, id: str, type: NotificationRulesType, **kwargs):
        """
        Notification rules allow full control over notifications generated by the various Datadog security products.
        They allow users to define the conditions under which a notification should be generated (based on rule severities,
        rule types, rule tags, and so on), and the targets to notify.
        A notification rule is composed of a rule ID, a rule type, and the rule attributes. All fields are required.

        :param attributes: Attributes of the notification rule.
        :type attributes: NotificationRuleAttributes

        :param id: The ID of a notification rule.
        :type id: str

        :param type: The rule type associated to notification rules.
        :type type: NotificationRulesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
