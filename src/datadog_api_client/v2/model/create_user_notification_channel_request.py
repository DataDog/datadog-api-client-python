# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_notification_channel_data import CreateNotificationChannelData


class CreateUserNotificationChannelRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_notification_channel_data import CreateNotificationChannelData

        return {
            "data": (CreateNotificationChannelData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CreateNotificationChannelData, **kwargs):
        """
        A top-level wrapper for creating a notification channel for a user

        :param data: Data for creating an on-call notification channel
        :type data: CreateNotificationChannelData
        """
        super().__init__(kwargs)

        self_.data = data
