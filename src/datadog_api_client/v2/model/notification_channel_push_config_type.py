# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationChannelPushConfigType(ModelSimple):
    """
    Indicates that the notification channel is a mobile device for push notifications

    :param value: If omitted defaults to "push". Must be one of ["push"].
    :type value: str
    """

    allowed_values = {
        "push",
    }
    PUSH: ClassVar["NotificationChannelPushConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationChannelPushConfigType.PUSH = NotificationChannelPushConfigType("push")
