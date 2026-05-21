# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_inference_code import LLMObsInferenceCode
    from datadog_api_client.v2.model.llm_obs_internal_reasoning import LLMObsInternalReasoning
    from datadog_api_client.v2.model.llm_obs_inference_tool import LLMObsInferenceTool


class LLMObsInferenceRunResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_inference_code import LLMObsInferenceCode
        from datadog_api_client.v2.model.llm_obs_internal_reasoning import LLMObsInternalReasoning
        from datadog_api_client.v2.model.llm_obs_inference_tool import LLMObsInferenceTool

        return {
            "assessment": (str, none_type),
            "content": (str,),
            "finish_reason": (str,),
            "inference_codes": ([LLMObsInferenceCode],),
            "input_tokens": (int,),
            "internal_reasoning": (LLMObsInternalReasoning,),
            "latency": (int,),
            "output_tokens": (int,),
            "tools": ([LLMObsInferenceTool],),
            "total_tokens": (int,),
        }

    attribute_map = {
        "assessment": "assessment",
        "content": "content",
        "finish_reason": "finish_reason",
        "inference_codes": "inference_codes",
        "input_tokens": "input_tokens",
        "internal_reasoning": "internal_reasoning",
        "latency": "latency",
        "output_tokens": "output_tokens",
        "tools": "tools",
        "total_tokens": "total_tokens",
    }

    def __init__(
        self_,
        assessment: Union[str, none_type],
        content: str,
        finish_reason: str,
        inference_codes: List[LLMObsInferenceCode],
        input_tokens: int,
        latency: int,
        output_tokens: int,
        tools: List[LLMObsInferenceTool],
        total_tokens: int,
        internal_reasoning: Union[LLMObsInternalReasoning, UnsetType] = unset,
        **kwargs,
    ):
        """
        The output of a completed LLM inference call.

        :param assessment: An optional assessment of the inference output quality.
        :type assessment: str, none_type

        :param content: The text content of the model response.
        :type content: str

        :param finish_reason: The reason the model stopped generating tokens.
        :type finish_reason: str

        :param inference_codes: List of generated code snippets for the inference configuration.
        :type inference_codes: [LLMObsInferenceCode]

        :param input_tokens: Number of input tokens consumed.
        :type input_tokens: int

        :param internal_reasoning: The model's internal reasoning or thinking output, if available.
        :type internal_reasoning: LLMObsInternalReasoning, optional

        :param latency: Request latency in milliseconds.
        :type latency: int

        :param output_tokens: Number of output tokens generated.
        :type output_tokens: int

        :param tools: List of tools available to the model.
        :type tools: [LLMObsInferenceTool]

        :param total_tokens: Total tokens used (input plus output).
        :type total_tokens: int
        """
        if internal_reasoning is not unset:
            kwargs["internal_reasoning"] = internal_reasoning
        super().__init__(kwargs)

        self_.assessment = assessment
        self_.content = content
        self_.finish_reason = finish_reason
        self_.inference_codes = inference_codes
        self_.input_tokens = input_tokens
        self_.latency = latency
        self_.output_tokens = output_tokens
        self_.tools = tools
        self_.total_tokens = total_tokens
