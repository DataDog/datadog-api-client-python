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
    from datadog_api_client.v2.model.llm_obs_span_tool_call import LLMObsSpanToolCall
    from datadog_api_client.v2.model.llm_obs_span_tool_result import LLMObsSpanToolResult


class LLMObsSpanMessage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_span_tool_call import LLMObsSpanToolCall
        from datadog_api_client.v2.model.llm_obs_span_tool_result import LLMObsSpanToolResult

        return {
            "content": (str,),
            "id": (str,),
            "role": (str,),
            "tool_calls": ([LLMObsSpanToolCall],),
            "tool_results": ([LLMObsSpanToolResult],),
        }

    attribute_map = {
        "content": "content",
        "id": "id",
        "role": "role",
        "tool_calls": "tool_calls",
        "tool_results": "tool_results",
    }

    def __init__(
        self_,
        content: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        role: Union[str, UnsetType] = unset,
        tool_calls: Union[List[LLMObsSpanToolCall], UnsetType] = unset,
        tool_results: Union[List[LLMObsSpanToolResult], UnsetType] = unset,
        **kwargs,
    ):
        """
        A single message in a span input or output.

        :param content: Text content of the message.
        :type content: str, optional

        :param id: Unique identifier of the message.
        :type id: str, optional

        :param role: Role of the message sender (e.g., user, assistant, system).
        :type role: str, optional

        :param tool_calls: Tool calls made in this message.
        :type tool_calls: [LLMObsSpanToolCall], optional

        :param tool_results: Tool results returned in this message.
        :type tool_results: [LLMObsSpanToolResult], optional
        """
        if content is not unset:
            kwargs["content"] = content
        if id is not unset:
            kwargs["id"] = id
        if role is not unset:
            kwargs["role"] = role
        if tool_calls is not unset:
            kwargs["tool_calls"] = tool_calls
        if tool_results is not unset:
            kwargs["tool_results"] = tool_results
        super().__init__(kwargs)
