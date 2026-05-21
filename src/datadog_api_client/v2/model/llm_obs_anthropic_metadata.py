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
    from datadog_api_client.v2.model.llm_obs_anthropic_effort import LLMObsAnthropicEffort
    from datadog_api_client.v2.model.llm_obs_anthropic_thinking_config import LLMObsAnthropicThinkingConfig


class LLMObsAnthropicMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_anthropic_effort import LLMObsAnthropicEffort
        from datadog_api_client.v2.model.llm_obs_anthropic_thinking_config import LLMObsAnthropicThinkingConfig

        return {
            "effort": (LLMObsAnthropicEffort,),
            "thinking": (LLMObsAnthropicThinkingConfig,),
        }

    attribute_map = {
        "effort": "effort",
        "thinking": "thinking",
    }

    def __init__(
        self_,
        effort: Union[LLMObsAnthropicEffort, none_type, UnsetType] = unset,
        thinking: Union[LLMObsAnthropicThinkingConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        Anthropic-specific metadata for an inference request.

        :param effort: The effort level for Anthropic inference.
        :type effort: LLMObsAnthropicEffort, none_type, optional

        :param thinking: Configuration for Anthropic extended thinking feature.
        :type thinking: LLMObsAnthropicThinkingConfig, optional
        """
        if effort is not unset:
            kwargs["effort"] = effort
        if thinking is not unset:
            kwargs["thinking"] = thinking
        super().__init__(kwargs)
