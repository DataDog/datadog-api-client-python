# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationChannelType(ModelSimple):
    """
    Indicates that the resource is of type 'notification_channels'.

    :param value: If omitted defaults to "notification_channels". Must be one of ["notification_channels"].
    :type value: str
    """

    allowed_values = {
        "notification_channels",
    }
    NOTIFICATION_CHANNELS: ClassVar["NotificationChannelType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationChannelType.NOTIFICATION_CHANNELS = NotificationChannelType("notification_channels")
