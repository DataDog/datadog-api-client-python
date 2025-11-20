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
    from datadog_api_client.v2.model.monitor_notification_rule_condition import MonitorNotificationRuleCondition


class MonitorNotificationRuleConditionalRecipients(ModelNormal):
    validations = {
        "conditions": {
            "max_items": 10,
            "min_items": 1,
        },
        "fallback_recipients": {
            "max_items": 20,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_condition import MonitorNotificationRuleCondition

        return {
            "conditions": ([MonitorNotificationRuleCondition],),
            "fallback_recipients": ([str],),
        }

    attribute_map = {
        "conditions": "conditions",
        "fallback_recipients": "fallback_recipients",
    }

    def __init__(
        self_,
        conditions: List[MonitorNotificationRuleCondition],
        fallback_recipients: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Use conditional recipients to define different recipients for different situations. Cannot be used with ``recipients``.

        :param conditions: Conditions of the notification rule.
        :type conditions: [MonitorNotificationRuleCondition]

        :param fallback_recipients: A list of recipients to notify. Uses the same format as the monitor ``message`` field. Must not start with an '@'. Cannot be used with ``conditional_recipients``.
        :type fallback_recipients: [str], optional
        """
        if fallback_recipients is not unset:
            kwargs["fallback_recipients"] = fallback_recipients
        super().__init__(kwargs)

        self_.conditions = conditions
