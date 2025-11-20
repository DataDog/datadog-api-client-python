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
    from datadog_api_client.v2.model.monitor_notification_rule_conditional_recipients import (
        MonitorNotificationRuleConditionalRecipients,
    )
    from datadog_api_client.v2.model.monitor_notification_rule_filter import MonitorNotificationRuleFilter
    from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags
    from datadog_api_client.v2.model.monitor_notification_rule_filter_scope import MonitorNotificationRuleFilterScope


class MonitorNotificationRuleAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 1000,
            "min_length": 1,
        },
        "recipients": {
            "max_items": 20,
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_conditional_recipients import (
            MonitorNotificationRuleConditionalRecipients,
        )
        from datadog_api_client.v2.model.monitor_notification_rule_filter import MonitorNotificationRuleFilter

        return {
            "conditional_recipients": (MonitorNotificationRuleConditionalRecipients,),
            "filter": (MonitorNotificationRuleFilter,),
            "name": (str,),
            "recipients": ([str],),
        }

    attribute_map = {
        "conditional_recipients": "conditional_recipients",
        "filter": "filter",
        "name": "name",
        "recipients": "recipients",
    }

    def __init__(
        self_,
        name: str,
        conditional_recipients: Union[MonitorNotificationRuleConditionalRecipients, UnsetType] = unset,
        filter: Union[
            MonitorNotificationRuleFilter,
            MonitorNotificationRuleFilterTags,
            MonitorNotificationRuleFilterScope,
            UnsetType,
        ] = unset,
        recipients: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the monitor notification rule.

        :param conditional_recipients: Use conditional recipients to define different recipients for different situations. Cannot be used with ``recipients``.
        :type conditional_recipients: MonitorNotificationRuleConditionalRecipients, optional

        :param filter: Filter used to associate the notification rule with monitors.
        :type filter: MonitorNotificationRuleFilter, optional

        :param name: The name of the monitor notification rule.
        :type name: str

        :param recipients: A list of recipients to notify. Uses the same format as the monitor ``message`` field. Must not start with an '@'. Cannot be used with ``conditional_recipients``.
        :type recipients: [str], optional
        """
        if conditional_recipients is not unset:
            kwargs["conditional_recipients"] = conditional_recipients
        if filter is not unset:
            kwargs["filter"] = filter
        if recipients is not unset:
            kwargs["recipients"] = recipients
        super().__init__(kwargs)

        self_.name = name
