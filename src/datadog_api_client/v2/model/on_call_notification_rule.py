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
    from datadog_api_client.v2.model.on_call_notification_rule_data import OnCallNotificationRuleData
    from datadog_api_client.v2.model.on_call_notification_rules_included import OnCallNotificationRulesIncluded
    from datadog_api_client.v2.model.notification_channel_data import NotificationChannelData


class OnCallNotificationRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_notification_rule_data import OnCallNotificationRuleData
        from datadog_api_client.v2.model.on_call_notification_rules_included import OnCallNotificationRulesIncluded

        return {
            "data": (OnCallNotificationRuleData,),
            "included": ([OnCallNotificationRulesIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: OnCallNotificationRuleData,
        included: Union[List[Union[OnCallNotificationRulesIncluded, NotificationChannelData]], UnsetType] = unset,
        **kwargs,
    ):
        """
        A top-level wrapper for a notification rule

        :param data: Data for an on-call notification rule
        :type data: OnCallNotificationRuleData

        :param included:
        :type included: [OnCallNotificationRulesIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
