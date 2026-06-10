# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotificationRulePreviewResponseType(ModelSimple):
    """
    The type of the notification preview response.

    :param value: If omitted defaults to "notification_preview_response". Must be one of ["notification_preview_response"].
    :type value: str
    """

    allowed_values = {
        "notification_preview_response",
    }
    NOTIFICATION_PREVIEW_RESPONSE: ClassVar["NotificationRulePreviewResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotificationRulePreviewResponseType.NOTIFICATION_PREVIEW_RESPONSE = NotificationRulePreviewResponseType(
    "notification_preview_response"
)
