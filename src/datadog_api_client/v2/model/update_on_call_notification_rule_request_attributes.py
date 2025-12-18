# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_notification_rule_category import OnCallNotificationRuleCategory
    from datadog_api_client.v2.model.on_call_notification_rule_channel_settings import (
        OnCallNotificationRuleChannelSettings,
    )
    from datadog_api_client.v2.model.on_call_phone_notification_rule_settings import OnCallPhoneNotificationRuleSettings


class UpdateOnCallNotificationRuleRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_notification_rule_category import OnCallNotificationRuleCategory
        from datadog_api_client.v2.model.on_call_notification_rule_channel_settings import (
            OnCallNotificationRuleChannelSettings,
        )

        return {
            "category": (OnCallNotificationRuleCategory,),
            "channel_settings": (OnCallNotificationRuleChannelSettings,),
            "delay_minutes": (int,),
        }

    attribute_map = {
        "category": "category",
        "channel_settings": "channel_settings",
        "delay_minutes": "delay_minutes",
    }

    def __init__(
        self_,
        category: Union[OnCallNotificationRuleCategory, UnsetType] = unset,
        channel_settings: Union[
            OnCallNotificationRuleChannelSettings, OnCallPhoneNotificationRuleSettings, UnsetType
        ] = unset,
        delay_minutes: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or modifying an on-call notification rule.

        :param category: Specifies the category a notification rule will apply to
        :type category: OnCallNotificationRuleCategory, optional

        :param channel_settings: Defines the configuration for a channel associated with a notification rule
        :type channel_settings: OnCallNotificationRuleChannelSettings, optional

        :param delay_minutes: The number of minutes that will elapse before this rule is evaluated.  0 indicates immediate evaluation
        :type delay_minutes: int, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if channel_settings is not unset:
            kwargs["channel_settings"] = channel_settings
        if delay_minutes is not unset:
            kwargs["delay_minutes"] = delay_minutes
        super().__init__(kwargs)
