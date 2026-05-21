# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnthropicEffort(ModelSimple):
    """
    The effort level for Anthropic inference.

    :param value: Must be one of ["low", "medium", "high", "max"].
    :type value: str
    """

    allowed_values = {
        "low",
        "medium",
        "high",
        "max",
    }
    LOW: ClassVar["LLMObsAnthropicEffort"]
    MEDIUM: ClassVar["LLMObsAnthropicEffort"]
    HIGH: ClassVar["LLMObsAnthropicEffort"]
    MAX: ClassVar["LLMObsAnthropicEffort"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnthropicEffort.LOW = LLMObsAnthropicEffort("low")
LLMObsAnthropicEffort.MEDIUM = LLMObsAnthropicEffort("medium")
LLMObsAnthropicEffort.HIGH = LLMObsAnthropicEffort("high")
LLMObsAnthropicEffort.MAX = LLMObsAnthropicEffort("max")
