# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_notification_rule_filter import MonitorNotificationRuleFilter
    from datadog_api_client.v2.model.monitor_notification_rule_filter_tags import MonitorNotificationRuleFilterTags


class MonitorNotificationRuleResponseAttributes(ModelNormal):
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
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_filter import MonitorNotificationRuleFilter

        return {
            "created": (datetime,),
            "filter": (MonitorNotificationRuleFilter,),
            "modified": (datetime,),
            "name": (str,),
            "recipients": ([str],),
        }

    attribute_map = {
        "created": "created",
        "filter": "filter",
        "modified": "modified",
        "name": "name",
        "recipients": "recipients",
    }

    def __init__(
        self_,
        created: Union[datetime, UnsetType] = unset,
        filter: Union[MonitorNotificationRuleFilter, MonitorNotificationRuleFilterTags, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        recipients: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the monitor notification rule.

        :param created: Creation time of the monitor notification rule.
        :type created: datetime, optional

        :param filter: Filter used to associate the notification rule with monitors.
        :type filter: MonitorNotificationRuleFilter, optional

        :param modified: Time the monitor notification rule was last modified.
        :type modified: datetime, optional

        :param name: The name of the monitor notification rule.
        :type name: str, optional

        :param recipients: A list of recipients to notify. Uses the same format as the monitor ``message`` field. Must not start with an '@'.
        :type recipients: [str], optional
        """
        if created is not unset:
            kwargs["created"] = created
        if filter is not unset:
            kwargs["filter"] = filter
        if modified is not unset:
            kwargs["modified"] = modified
        if name is not unset:
            kwargs["name"] = name
        if recipients is not unset:
            kwargs["recipients"] = recipients
        super().__init__(kwargs)
