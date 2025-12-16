# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationChannelEmailConfigType(ModelSimple):
    """
    Indicates that the notification channel is an e-mail address

    :param value: If omitted defaults to "email". Must be one of ["email"].
    :type value: str
    """

    allowed_values = {
        "email",
    }
    EMAIL: ClassVar["NotificationChannelEmailConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationChannelEmailConfigType.EMAIL = NotificationChannelEmailConfigType("email")
