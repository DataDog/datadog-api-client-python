# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_tool_call_function import AIGuardToolCallFunction


class AIGuardToolCall(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_tool_call_function import AIGuardToolCallFunction

        return {
            "function": (AIGuardToolCallFunction,),
            "id": (str,),
        }

    attribute_map = {
        "function": "function",
        "id": "id",
    }

    def __init__(self_, function: AIGuardToolCallFunction, id: str, **kwargs):
        """
        A tool call issued by the assistant.

        :param function: The function definition within a tool call.
        :type function: AIGuardToolCallFunction

        :param id: The unique identifier of the tool call.
        :type id: str
        """
        super().__init__(kwargs)

        self_.function = function
        self_.id = id
