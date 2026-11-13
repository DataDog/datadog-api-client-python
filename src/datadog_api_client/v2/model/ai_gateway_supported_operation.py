# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewaySupportedOperation(ModelSimple):
    """
    Operation supported by an AI Gateway model.

    :param value: Must be one of ["ANTHROPIC_MESSAGES", "ANTHROPIC_COUNT_TOKENS", "OPENAI_CHAT_COMPLETIONS", "OPENAI_RESPONSES", "OPENAI_WEB_SEARCH", "OPENAI_EMBEDDINGS", "OPENAI_DECISIONS", "SYSTEM_ONE", "GEMINI_GENERATE_CONTENT", "GEMINI_RAW_PREDICTIONS"].
    :type value: str
    """

    allowed_values = {
        "ANTHROPIC_MESSAGES",
        "ANTHROPIC_COUNT_TOKENS",
        "OPENAI_CHAT_COMPLETIONS",
        "OPENAI_RESPONSES",
        "OPENAI_WEB_SEARCH",
        "OPENAI_EMBEDDINGS",
        "OPENAI_DECISIONS",
        "SYSTEM_ONE",
        "GEMINI_GENERATE_CONTENT",
        "GEMINI_RAW_PREDICTIONS",
    }
    ANTHROPIC_MESSAGES: ClassVar["AiGatewaySupportedOperation"]
    ANTHROPIC_COUNT_TOKENS: ClassVar["AiGatewaySupportedOperation"]
    OPENAI_CHAT_COMPLETIONS: ClassVar["AiGatewaySupportedOperation"]
    OPENAI_RESPONSES: ClassVar["AiGatewaySupportedOperation"]
    OPENAI_WEB_SEARCH: ClassVar["AiGatewaySupportedOperation"]
    OPENAI_EMBEDDINGS: ClassVar["AiGatewaySupportedOperation"]
    OPENAI_DECISIONS: ClassVar["AiGatewaySupportedOperation"]
    SYSTEM_ONE: ClassVar["AiGatewaySupportedOperation"]
    GEMINI_GENERATE_CONTENT: ClassVar["AiGatewaySupportedOperation"]
    GEMINI_RAW_PREDICTIONS: ClassVar["AiGatewaySupportedOperation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewaySupportedOperation.ANTHROPIC_MESSAGES = AiGatewaySupportedOperation("ANTHROPIC_MESSAGES")
AiGatewaySupportedOperation.ANTHROPIC_COUNT_TOKENS = AiGatewaySupportedOperation("ANTHROPIC_COUNT_TOKENS")
AiGatewaySupportedOperation.OPENAI_CHAT_COMPLETIONS = AiGatewaySupportedOperation("OPENAI_CHAT_COMPLETIONS")
AiGatewaySupportedOperation.OPENAI_RESPONSES = AiGatewaySupportedOperation("OPENAI_RESPONSES")
AiGatewaySupportedOperation.OPENAI_WEB_SEARCH = AiGatewaySupportedOperation("OPENAI_WEB_SEARCH")
AiGatewaySupportedOperation.OPENAI_EMBEDDINGS = AiGatewaySupportedOperation("OPENAI_EMBEDDINGS")
AiGatewaySupportedOperation.OPENAI_DECISIONS = AiGatewaySupportedOperation("OPENAI_DECISIONS")
AiGatewaySupportedOperation.SYSTEM_ONE = AiGatewaySupportedOperation("SYSTEM_ONE")
AiGatewaySupportedOperation.GEMINI_GENERATE_CONTENT = AiGatewaySupportedOperation("GEMINI_GENERATE_CONTENT")
AiGatewaySupportedOperation.GEMINI_RAW_PREDICTIONS = AiGatewaySupportedOperation("GEMINI_RAW_PREDICTIONS")
