# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsOpenAIReasoningEffort(ModelSimple):
    """
    The reasoning effort level for OpenAI models that support it.

    :param value: Must be one of ["none", "low", "medium", "high", "xhigh"].
    :type value: str
    """

    allowed_values = {
        "none",
        "low",
        "medium",
        "high",
        "xhigh",
    }
    NONE: ClassVar["LLMObsOpenAIReasoningEffort"]
    LOW: ClassVar["LLMObsOpenAIReasoningEffort"]
    MEDIUM: ClassVar["LLMObsOpenAIReasoningEffort"]
    HIGH: ClassVar["LLMObsOpenAIReasoningEffort"]
    XHIGH: ClassVar["LLMObsOpenAIReasoningEffort"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsOpenAIReasoningEffort.NONE = LLMObsOpenAIReasoningEffort("none")
LLMObsOpenAIReasoningEffort.LOW = LLMObsOpenAIReasoningEffort("low")
LLMObsOpenAIReasoningEffort.MEDIUM = LLMObsOpenAIReasoningEffort("medium")
LLMObsOpenAIReasoningEffort.HIGH = LLMObsOpenAIReasoningEffort("high")
LLMObsOpenAIReasoningEffort.XHIGH = LLMObsOpenAIReasoningEffort("xhigh")
