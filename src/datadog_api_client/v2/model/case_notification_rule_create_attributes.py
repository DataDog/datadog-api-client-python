# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.case_notification_rule_recipient import CaseNotificationRuleRecipient
    from datadog_api_client.v2.model.case_notification_rule_trigger import CaseNotificationRuleTrigger


class CaseNotificationRuleCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_notification_rule_recipient import CaseNotificationRuleRecipient
        from datadog_api_client.v2.model.case_notification_rule_trigger import CaseNotificationRuleTrigger

        return {
            "is_enabled": (bool,),
            "query": (str,),
            "recipients": ([CaseNotificationRuleRecipient],),
            "triggers": ([CaseNotificationRuleTrigger],),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "query": "query",
        "recipients": "recipients",
        "triggers": "triggers",
    }

    def __init__(
        self_,
        recipients: List[CaseNotificationRuleRecipient],
        triggers: List[CaseNotificationRuleTrigger],
        is_enabled: Union[bool, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notification rule creation attributes

        :param is_enabled: Whether the notification rule is enabled
        :type is_enabled: bool, optional

        :param query: Query to filter cases for this notification rule
        :type query: str, optional

        :param recipients: List of notification recipients
        :type recipients: [CaseNotificationRuleRecipient]

        :param triggers: List of triggers for this notification rule
        :type triggers: [CaseNotificationRuleTrigger]
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)

        self_.recipients = recipients
        self_.triggers = triggers
