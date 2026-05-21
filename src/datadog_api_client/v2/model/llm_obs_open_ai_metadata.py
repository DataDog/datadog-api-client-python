# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_open_ai_reasoning_effort import LLMObsOpenAIReasoningEffort
    from datadog_api_client.v2.model.llm_obs_open_ai_reasoning_summary import LLMObsOpenAIReasoningSummary


class LLMObsOpenAIMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_open_ai_reasoning_effort import LLMObsOpenAIReasoningEffort
        from datadog_api_client.v2.model.llm_obs_open_ai_reasoning_summary import LLMObsOpenAIReasoningSummary

        return {
            "reasoning_effort": (LLMObsOpenAIReasoningEffort,),
            "reasoning_summary": (LLMObsOpenAIReasoningSummary,),
        }

    attribute_map = {
        "reasoning_effort": "reasoning_effort",
        "reasoning_summary": "reasoning_summary",
    }

    def __init__(
        self_,
        reasoning_effort: Union[LLMObsOpenAIReasoningEffort, none_type, UnsetType] = unset,
        reasoning_summary: Union[LLMObsOpenAIReasoningSummary, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        OpenAI-specific metadata for an inference request.

        :param reasoning_effort: The reasoning effort level for OpenAI models that support it.
        :type reasoning_effort: LLMObsOpenAIReasoningEffort, none_type, optional

        :param reasoning_summary: The verbosity of the reasoning summary.
        :type reasoning_summary: LLMObsOpenAIReasoningSummary, none_type, optional
        """
        if reasoning_effort is not unset:
            kwargs["reasoning_effort"] = reasoning_effort
        if reasoning_summary is not unset:
            kwargs["reasoning_summary"] = reasoning_summary
        super().__init__(kwargs)
