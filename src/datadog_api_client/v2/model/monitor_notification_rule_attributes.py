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
    from datadog_api_client.v2.model.monitor_notification_rule_filter import MonitorNotificationRuleFilter
    from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags


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
        from datadog_api_client.v2.model.monitor_notification_rule_filter import MonitorNotificationRuleFilter

        return {
            "filter": (MonitorNotificationRuleFilter,),
            "name": (str,),
            "recipients": ([str],),
        }

    attribute_map = {
        "filter": "filter",
        "name": "name",
        "recipients": "recipients",
    }

    def __init__(
        self_,
        name: str,
        recipients: List[str],
        filter: Union[MonitorNotificationRuleFilter, MonitorNotificationRuleFilterTags, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the monitor notification rule.

        :param filter: Filter used to associate the notification rule with monitors.
        :type filter: MonitorNotificationRuleFilter, optional

        :param name: The name of the monitor notification rule.
        :type name: str

        :param recipients: A list of recipients to notify. Uses the same format as the monitor ``message`` field. Must not start with an '@'.
        :type recipients: [str]
        """
        if filter is not unset:
            kwargs["filter"] = filter
        super().__init__(kwargs)

        self_.name = name
        self_.recipients = recipients
