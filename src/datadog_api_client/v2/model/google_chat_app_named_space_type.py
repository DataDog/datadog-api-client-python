# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GoogleChatAppNamedSpaceType(ModelSimple):
    """
    Google Chat app named space resource type.

    :param value: If omitted defaults to "google-chat-app-named-space". Must be one of ["google-chat-app-named-space"].
    :type value: str
    """

    allowed_values = {
        "google-chat-app-named-space",
    }
    GOOGLE_CHAT_APP_NAMED_SPACE_TYPE: ClassVar["GoogleChatAppNamedSpaceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GoogleChatAppNamedSpaceType.GOOGLE_CHAT_APP_NAMED_SPACE_TYPE = GoogleChatAppNamedSpaceType(
    "google-chat-app-named-space"
)
