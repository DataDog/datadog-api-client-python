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
    from datadog_api_client.v2.model.notification_channel_attributes import NotificationChannelAttributes
    from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType


class NotificationChannelData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_attributes import NotificationChannelAttributes
        from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType

        return {
            "attributes": (NotificationChannelAttributes,),
            "id": (str,),
            "type": (NotificationChannelType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: NotificationChannelType,
        attributes: Union[NotificationChannelAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for an on-call notification channel

        :param attributes: Attributes for an on-call notification channel.
        :type attributes: NotificationChannelAttributes, optional

        :param id: Unique identifier for the channel
        :type id: str, optional

        :param type: Indicates that the resource is of type 'notification_channels'.
        :type type: NotificationChannelType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
