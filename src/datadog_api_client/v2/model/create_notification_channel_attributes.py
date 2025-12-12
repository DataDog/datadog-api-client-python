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
    from datadog_api_client.v2.model.create_notification_channel_config import CreateNotificationChannelConfig
    from datadog_api_client.v2.model.create_phone_notification_channel_config import (
        CreatePhoneNotificationChannelConfig,
    )
    from datadog_api_client.v2.model.create_email_notification_channel_config import (
        CreateEmailNotificationChannelConfig,
    )


class CreateNotificationChannelAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_notification_channel_config import CreateNotificationChannelConfig

        return {
            "config": (CreateNotificationChannelConfig,),
        }

    attribute_map = {
        "config": "config",
    }

    def __init__(
        self_,
        config: Union[
            CreateNotificationChannelConfig,
            CreatePhoneNotificationChannelConfig,
            CreateEmailNotificationChannelConfig,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an on-call notification channel.

        :param config: Defines the configuration for creating an On-Call notification channel
        :type config: CreateNotificationChannelConfig, optional
        """
        if config is not unset:
            kwargs["config"] = config
        super().__init__(kwargs)
