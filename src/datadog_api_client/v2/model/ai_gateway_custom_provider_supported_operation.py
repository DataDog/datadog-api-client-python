# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayCustomProviderSupportedOperation(ModelSimple):
    """
    Operation supported by a custom provider.

    :param value: Must be one of ["OPENAI_CHAT_COMPLETIONS", "OPENAI_RESPONSES", "ANTHROPIC_MESSAGES", "SYSTEM_ONE"].
    :type value: str
    """

    allowed_values = {
        "OPENAI_CHAT_COMPLETIONS",
        "OPENAI_RESPONSES",
        "ANTHROPIC_MESSAGES",
        "SYSTEM_ONE",
    }
    OPENAI_CHAT_COMPLETIONS: ClassVar["AiGatewayCustomProviderSupportedOperation"]
    OPENAI_RESPONSES: ClassVar["AiGatewayCustomProviderSupportedOperation"]
    ANTHROPIC_MESSAGES: ClassVar["AiGatewayCustomProviderSupportedOperation"]
    SYSTEM_ONE: ClassVar["AiGatewayCustomProviderSupportedOperation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayCustomProviderSupportedOperation.OPENAI_CHAT_COMPLETIONS = AiGatewayCustomProviderSupportedOperation(
    "OPENAI_CHAT_COMPLETIONS"
)
AiGatewayCustomProviderSupportedOperation.OPENAI_RESPONSES = AiGatewayCustomProviderSupportedOperation(
    "OPENAI_RESPONSES"
)
AiGatewayCustomProviderSupportedOperation.ANTHROPIC_MESSAGES = AiGatewayCustomProviderSupportedOperation(
    "ANTHROPIC_MESSAGES"
)
AiGatewayCustomProviderSupportedOperation.SYSTEM_ONE = AiGatewayCustomProviderSupportedOperation("SYSTEM_ONE")
