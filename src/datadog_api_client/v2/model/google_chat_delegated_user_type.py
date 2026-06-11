# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GoogleChatDelegatedUserType(ModelSimple):
    """
    Google Chat delegated user resource type.

    :param value: If omitted defaults to "google-chat-delegated-user". Must be one of ["google-chat-delegated-user"].
    :type value: str
    """

    allowed_values = {
        "google-chat-delegated-user",
    }
    GOOGLE_CHAT_DELEGATED_USER_TYPE: ClassVar["GoogleChatDelegatedUserType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GoogleChatDelegatedUserType.GOOGLE_CHAT_DELEGATED_USER_TYPE = GoogleChatDelegatedUserType("google-chat-delegated-user")
