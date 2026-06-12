# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AIGuardMessageRole(ModelSimple):
    """
    The role of the message author in the conversation.

    :param value: Must be one of ["user", "assistant", "system", "tool", "developer"].
    :type value: str
    """

    allowed_values = {
        "user",
        "assistant",
        "system",
        "tool",
        "developer",
    }
    USER: ClassVar["AIGuardMessageRole"]
    ASSISTANT: ClassVar["AIGuardMessageRole"]
    SYSTEM: ClassVar["AIGuardMessageRole"]
    TOOL: ClassVar["AIGuardMessageRole"]
    DEVELOPER: ClassVar["AIGuardMessageRole"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AIGuardMessageRole.USER = AIGuardMessageRole("user")
AIGuardMessageRole.ASSISTANT = AIGuardMessageRole("assistant")
AIGuardMessageRole.SYSTEM = AIGuardMessageRole("system")
AIGuardMessageRole.TOOL = AIGuardMessageRole("tool")
AIGuardMessageRole.DEVELOPER = AIGuardMessageRole("developer")
