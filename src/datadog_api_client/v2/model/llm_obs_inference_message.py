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
    from datadog_api_client.v2.model.llm_obs_inference_content import LLMObsInferenceContent
    from datadog_api_client.v2.model.llm_obs_inference_tool_call import LLMObsInferenceToolCall
    from datadog_api_client.v2.model.llm_obs_inference_tool_result import LLMObsInferenceToolResult


class LLMObsInferenceMessage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_inference_content import LLMObsInferenceContent
        from datadog_api_client.v2.model.llm_obs_inference_tool_call import LLMObsInferenceToolCall
        from datadog_api_client.v2.model.llm_obs_inference_tool_result import LLMObsInferenceToolResult

        return {
            "content": (str,),
            "contents": ([LLMObsInferenceContent],),
            "id": (str,),
            "role": (str,),
            "tool_calls": ([LLMObsInferenceToolCall],),
            "tool_results": ([LLMObsInferenceToolResult],),
        }

    attribute_map = {
        "content": "content",
        "contents": "contents",
        "id": "id",
        "role": "role",
        "tool_calls": "tool_calls",
        "tool_results": "tool_results",
    }

    def __init__(
        self_,
        content: Union[str, UnsetType] = unset,
        contents: Union[List[LLMObsInferenceContent], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        role: Union[str, UnsetType] = unset,
        tool_calls: Union[List[LLMObsInferenceToolCall], UnsetType] = unset,
        tool_results: Union[List[LLMObsInferenceToolResult], UnsetType] = unset,
        **kwargs,
    ):
        """
        A single message in an LLM inference conversation.

        :param content: Plain text content of the message.
        :type content: str, optional

        :param contents: List of structured content blocks in a message.
        :type contents: [LLMObsInferenceContent], optional

        :param id: Unique identifier for the message.
        :type id: str, optional

        :param role: The role of the message author.
        :type role: str, optional

        :param tool_calls: List of tool calls in a message.
        :type tool_calls: [LLMObsInferenceToolCall], optional

        :param tool_results: List of tool results in a message.
        :type tool_results: [LLMObsInferenceToolResult], optional
        """
        if content is not unset:
            kwargs["content"] = content
        if contents is not unset:
            kwargs["contents"] = contents
        if id is not unset:
            kwargs["id"] = id
        if role is not unset:
            kwargs["role"] = role
        if tool_calls is not unset:
            kwargs["tool_calls"] = tool_calls
        if tool_results is not unset:
            kwargs["tool_results"] = tool_results
        super().__init__(kwargs)
