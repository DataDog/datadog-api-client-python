# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayKnownProvider(ModelSimple):
    """
    Known provider implementation.

    :param value: Must be one of ["custom", "anthropic", "openai", "azure_openai", "bedrock", "gemini", "baseten", "fireworks", "together", "typesafe", "azure_foundry"].
    :type value: str
    """

    allowed_values = {
        "custom",
        "anthropic",
        "openai",
        "azure_openai",
        "bedrock",
        "gemini",
        "baseten",
        "fireworks",
        "together",
        "typesafe",
        "azure_foundry",
    }
    CUSTOM: ClassVar["AiGatewayKnownProvider"]
    ANTHROPIC: ClassVar["AiGatewayKnownProvider"]
    OPENAI: ClassVar["AiGatewayKnownProvider"]
    AZURE_OPENAI: ClassVar["AiGatewayKnownProvider"]
    BEDROCK: ClassVar["AiGatewayKnownProvider"]
    GEMINI: ClassVar["AiGatewayKnownProvider"]
    BASETEN: ClassVar["AiGatewayKnownProvider"]
    FIREWORKS: ClassVar["AiGatewayKnownProvider"]
    TOGETHER: ClassVar["AiGatewayKnownProvider"]
    TYPESAFE: ClassVar["AiGatewayKnownProvider"]
    AZURE_FOUNDRY: ClassVar["AiGatewayKnownProvider"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayKnownProvider.CUSTOM = AiGatewayKnownProvider("custom")
AiGatewayKnownProvider.ANTHROPIC = AiGatewayKnownProvider("anthropic")
AiGatewayKnownProvider.OPENAI = AiGatewayKnownProvider("openai")
AiGatewayKnownProvider.AZURE_OPENAI = AiGatewayKnownProvider("azure_openai")
AiGatewayKnownProvider.BEDROCK = AiGatewayKnownProvider("bedrock")
AiGatewayKnownProvider.GEMINI = AiGatewayKnownProvider("gemini")
AiGatewayKnownProvider.BASETEN = AiGatewayKnownProvider("baseten")
AiGatewayKnownProvider.FIREWORKS = AiGatewayKnownProvider("fireworks")
AiGatewayKnownProvider.TOGETHER = AiGatewayKnownProvider("together")
AiGatewayKnownProvider.TYPESAFE = AiGatewayKnownProvider("typesafe")
AiGatewayKnownProvider.AZURE_FOUNDRY = AiGatewayKnownProvider("azure_foundry")
