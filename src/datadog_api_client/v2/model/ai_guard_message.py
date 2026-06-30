# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_message_content import AIGuardMessageContent
    from datadog_api_client.v2.model.ai_guard_message_role import AIGuardMessageRole
    from datadog_api_client.v2.model.ai_guard_tool_call import AIGuardToolCall
    from datadog_api_client.v2.model.ai_guard_content_part import AIGuardContentPart


class AIGuardMessage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_message_content import AIGuardMessageContent
        from datadog_api_client.v2.model.ai_guard_message_role import AIGuardMessageRole
        from datadog_api_client.v2.model.ai_guard_tool_call import AIGuardToolCall

        return {
            "content": (AIGuardMessageContent,),
            "role": (AIGuardMessageRole,),
            "tool_call_id": (str,),
            "tool_calls": ([AIGuardToolCall],),
        }

    attribute_map = {
        "content": "content",
        "role": "role",
        "tool_call_id": "tool_call_id",
        "tool_calls": "tool_calls",
    }

    def __init__(
        self_,
        role: AIGuardMessageRole,
        content: Union[AIGuardMessageContent, str, List[AIGuardContentPart], UnsetType] = unset,
        tool_call_id: Union[str, UnsetType] = unset,
        tool_calls: Union[List[AIGuardToolCall], UnsetType] = unset,
        **kwargs,
    ):
        """
        A single message in the conversation to evaluate.

        :param content: The message content, either a plain string or an array of content parts.
        :type content: AIGuardMessageContent, optional

        :param role: The role of the message author in the conversation.
        :type role: AIGuardMessageRole

        :param tool_call_id: The ID of the tool call this message is responding to, required for tool messages.
        :type tool_call_id: str, optional

        :param tool_calls: Tool calls issued by the assistant in this message.
        :type tool_calls: [AIGuardToolCall], optional
        """
        if content is not unset:
            kwargs["content"] = content
        if tool_call_id is not unset:
            kwargs["tool_call_id"] = tool_call_id
        if tool_calls is not unset:
            kwargs["tool_calls"] = tool_calls
        super().__init__(kwargs)

        self_.role = role
