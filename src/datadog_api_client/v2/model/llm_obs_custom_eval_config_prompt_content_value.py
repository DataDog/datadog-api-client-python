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
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_tool_call import (
        LLMObsCustomEvalConfigPromptToolCall,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_tool_result import (
        LLMObsCustomEvalConfigPromptToolResult,
    )


class LLMObsCustomEvalConfigPromptContentValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_tool_call import (
            LLMObsCustomEvalConfigPromptToolCall,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_prompt_tool_result import (
            LLMObsCustomEvalConfigPromptToolResult,
        )

        return {
            "text": (str,),
            "tool_call": (LLMObsCustomEvalConfigPromptToolCall,),
            "tool_call_result": (LLMObsCustomEvalConfigPromptToolResult,),
        }

    attribute_map = {
        "text": "text",
        "tool_call": "tool_call",
        "tool_call_result": "tool_call_result",
    }

    def __init__(
        self_,
        text: Union[str, UnsetType] = unset,
        tool_call: Union[LLMObsCustomEvalConfigPromptToolCall, UnsetType] = unset,
        tool_call_result: Union[LLMObsCustomEvalConfigPromptToolResult, UnsetType] = unset,
        **kwargs,
    ):
        """
        Value of a prompt message content block.

        :param text: Text content of the message block.
        :type text: str, optional

        :param tool_call: A tool call within a prompt message.
        :type tool_call: LLMObsCustomEvalConfigPromptToolCall, optional

        :param tool_call_result: A tool call result within a prompt message.
        :type tool_call_result: LLMObsCustomEvalConfigPromptToolResult, optional
        """
        if text is not unset:
            kwargs["text"] = text
        if tool_call is not unset:
            kwargs["tool_call"] = tool_call
        if tool_call_result is not unset:
            kwargs["tool_call_result"] = tool_call_result
        super().__init__(kwargs)
