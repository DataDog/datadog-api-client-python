# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_inference_tool_call import LLMObsInferenceToolCall
    from datadog_api_client.v2.model.llm_obs_inference_tool_result import LLMObsInferenceToolResult


class LLMObsInferenceContentValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_inference_tool_call import LLMObsInferenceToolCall
        from datadog_api_client.v2.model.llm_obs_inference_tool_result import LLMObsInferenceToolResult

        return {
            "text": (str,),
            "tool_call": (LLMObsInferenceToolCall,),
            "tool_call_result": (LLMObsInferenceToolResult,),
        }

    attribute_map = {
        "text": "text",
        "tool_call": "tool_call",
        "tool_call_result": "tool_call_result",
    }

    def __init__(
        self_,
        text: Union[str, UnsetType] = unset,
        tool_call: Union[LLMObsInferenceToolCall, UnsetType] = unset,
        tool_call_result: Union[LLMObsInferenceToolResult, UnsetType] = unset,
        **kwargs,
    ):
        """
        The typed value of a message content block.

        :param text: Plain text content.
        :type text: str, optional

        :param tool_call: A tool call made during LLM inference.
        :type tool_call: LLMObsInferenceToolCall, optional

        :param tool_call_result: The result returned by a tool call during LLM inference.
        :type tool_call_result: LLMObsInferenceToolResult, optional
        """
        if text is not unset:
            kwargs["text"] = text
        if tool_call is not unset:
            kwargs["tool_call"] = tool_call
        if tool_call_result is not unset:
            kwargs["tool_call_result"] = tool_call_result
        super().__init__(kwargs)
