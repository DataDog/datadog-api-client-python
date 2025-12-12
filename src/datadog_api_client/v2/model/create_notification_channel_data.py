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
    from datadog_api_client.v2.model.create_notification_channel_attributes import CreateNotificationChannelAttributes
    from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType


class CreateNotificationChannelData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_notification_channel_attributes import (
            CreateNotificationChannelAttributes,
        )
        from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType

        return {
            "attributes": (CreateNotificationChannelAttributes,),
            "type": (NotificationChannelType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: NotificationChannelType,
        attributes: Union[CreateNotificationChannelAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for creating an on-call notification channel

        :param attributes: Attributes for creating an on-call notification channel.
        :type attributes: CreateNotificationChannelAttributes, optional

        :param type: Indicates that the resource is of type 'notification_channels'.
        :type type: NotificationChannelType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
