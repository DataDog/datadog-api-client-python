# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GoogleChatTargetAudienceType(ModelSimple):
    """
    Google Chat target audience resource type.

    :param value: If omitted defaults to "google-chat-target-audience". Must be one of ["google-chat-target-audience"].
    :type value: str
    """

    allowed_values = {
        "google-chat-target-audience",
    }
    GOOGLE_CHAT_TARGET_AUDIENCE_TYPE: ClassVar["GoogleChatTargetAudienceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GoogleChatTargetAudienceType.GOOGLE_CHAT_TARGET_AUDIENCE_TYPE = GoogleChatTargetAudienceType(
    "google-chat-target-audience"
)
