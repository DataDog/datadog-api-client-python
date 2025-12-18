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
    from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType


class OnCallNotificationRuleChannelRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_type import NotificationChannelType

        return {
            "id": (str,),
            "type": (NotificationChannelType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: Union[str, UnsetType] = unset, type: Union[NotificationChannelType, UnsetType] = unset, **kwargs
    ):
        """
        Channel relationship data for creating a notification rule

        :param id: ID of the notification channel
        :type id: str, optional

        :param type: Indicates that the resource is of type 'notification_channels'.
        :type type: NotificationChannelType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
