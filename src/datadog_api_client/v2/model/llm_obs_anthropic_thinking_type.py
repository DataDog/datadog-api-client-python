# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnthropicThinkingType(ModelSimple):
    """
    The thinking mode for Anthropic extended thinking.

    :param value: Must be one of ["enabled", "disabled", "adaptive"].
    :type value: str
    """

    allowed_values = {
        "enabled",
        "disabled",
        "adaptive",
    }
    ENABLED: ClassVar["LLMObsAnthropicThinkingType"]
    DISABLED: ClassVar["LLMObsAnthropicThinkingType"]
    ADAPTIVE: ClassVar["LLMObsAnthropicThinkingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnthropicThinkingType.ENABLED = LLMObsAnthropicThinkingType("enabled")
LLMObsAnthropicThinkingType.DISABLED = LLMObsAnthropicThinkingType("disabled")
LLMObsAnthropicThinkingType.ADAPTIVE = LLMObsAnthropicThinkingType("adaptive")
