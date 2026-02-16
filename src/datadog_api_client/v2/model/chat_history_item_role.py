# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChatHistoryItemRole(ModelSimple):
    """
    The role of the message sender.

    :param value: Must be one of ["user", "assistant"].
    :type value: str
    """

    allowed_values = {
        "user",
        "assistant",
    }
    USER: ClassVar["ChatHistoryItemRole"]
    ASSISTANT: ClassVar["ChatHistoryItemRole"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChatHistoryItemRole.USER = ChatHistoryItemRole("user")
ChatHistoryItemRole.ASSISTANT = ChatHistoryItemRole("assistant")
