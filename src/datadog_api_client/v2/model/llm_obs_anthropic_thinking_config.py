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
    from datadog_api_client.v2.model.llm_obs_anthropic_thinking_type import LLMObsAnthropicThinkingType


class LLMObsAnthropicThinkingConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_anthropic_thinking_type import LLMObsAnthropicThinkingType

        return {
            "budget_tokens": (int, none_type),
            "type": (LLMObsAnthropicThinkingType,),
        }

    attribute_map = {
        "budget_tokens": "budget_tokens",
        "type": "type",
    }

    def __init__(
        self_, type: LLMObsAnthropicThinkingType, budget_tokens: Union[int, none_type, UnsetType] = unset, **kwargs
    ):
        """
        Configuration for Anthropic extended thinking feature.

        :param budget_tokens: Maximum token budget for extended thinking. Required when type is ``enabled``.
        :type budget_tokens: int, none_type, optional

        :param type: The thinking mode for Anthropic extended thinking.
        :type type: LLMObsAnthropicThinkingType
        """
        if budget_tokens is not unset:
            kwargs["budget_tokens"] = budget_tokens
        super().__init__(kwargs)

        self_.type = type
