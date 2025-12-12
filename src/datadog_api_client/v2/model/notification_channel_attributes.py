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
    from datadog_api_client.v2.model.notification_channel_config import NotificationChannelConfig
    from datadog_api_client.v2.model.notification_channel_phone_config import NotificationChannelPhoneConfig
    from datadog_api_client.v2.model.notification_channel_email_config import NotificationChannelEmailConfig
    from datadog_api_client.v2.model.notification_channel_push_config import NotificationChannelPushConfig


class NotificationChannelAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_config import NotificationChannelConfig

        return {
            "active": (bool,),
            "config": (NotificationChannelConfig,),
        }

    attribute_map = {
        "active": "active",
        "config": "config",
    }

    def __init__(
        self_,
        active: Union[bool, UnsetType] = unset,
        config: Union[
            NotificationChannelConfig,
            NotificationChannelPhoneConfig,
            NotificationChannelEmailConfig,
            NotificationChannelPushConfig,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Attributes for an on-call notification channel.

        :param active: Whether the notification channel is currently active.
        :type active: bool, optional

        :param config: Defines the configuration for an On-Call notification channel
        :type config: NotificationChannelConfig, optional
        """
        if active is not unset:
            kwargs["active"] = active
        if config is not unset:
            kwargs["config"] = config
        super().__init__(kwargs)
