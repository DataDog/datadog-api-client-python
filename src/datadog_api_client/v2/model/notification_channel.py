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
    from datadog_api_client.v2.model.notification_channel_data import NotificationChannelData


class NotificationChannel(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notification_channel_data import NotificationChannelData

        return {
            "data": (NotificationChannelData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[NotificationChannelData, UnsetType] = unset, **kwargs):
        """
        A top-level wrapper for a user notification channel

        :param data: Data for an on-call notification channel
        :type data: NotificationChannelData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
