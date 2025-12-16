# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationChannelEmailFormatType(ModelSimple):
    """
    Specifies the format of the e-mail that is sent for On-Call notifications

    :param value: If omitted defaults to "html". Must be one of ["html", "text"].
    :type value: str
    """

    allowed_values = {
        "html",
        "text",
    }
    HTML: ClassVar["NotificationChannelEmailFormatType"]
    TEXT: ClassVar["NotificationChannelEmailFormatType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationChannelEmailFormatType.HTML = NotificationChannelEmailFormatType("html")
NotificationChannelEmailFormatType.TEXT = NotificationChannelEmailFormatType("text")
