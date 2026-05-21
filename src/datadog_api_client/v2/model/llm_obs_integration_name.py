# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsIntegrationName(ModelSimple):
    """
    The name of a supported LLM provider integration.

    :param value: Must be one of ["openai", "amazon_bedrock", "anthropic", "azure_openai", "vertex_ai", "llmproxy"].
    :type value: str
    """

    allowed_values = {
        "openai",
        "amazon_bedrock",
        "anthropic",
        "azure_openai",
        "vertex_ai",
        "llmproxy",
    }
    OPENAI: ClassVar["LLMObsIntegrationName"]
    AMAZON_BEDROCK: ClassVar["LLMObsIntegrationName"]
    ANTHROPIC: ClassVar["LLMObsIntegrationName"]
    AZURE_OPENAI: ClassVar["LLMObsIntegrationName"]
    VERTEX_AI: ClassVar["LLMObsIntegrationName"]
    LLMPROXY: ClassVar["LLMObsIntegrationName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsIntegrationName.OPENAI = LLMObsIntegrationName("openai")
LLMObsIntegrationName.AMAZON_BEDROCK = LLMObsIntegrationName("amazon_bedrock")
LLMObsIntegrationName.ANTHROPIC = LLMObsIntegrationName("anthropic")
LLMObsIntegrationName.AZURE_OPENAI = LLMObsIntegrationName("azure_openai")
LLMObsIntegrationName.VERTEX_AI = LLMObsIntegrationName("vertex_ai")
LLMObsIntegrationName.LLMPROXY = LLMObsIntegrationName("llmproxy")
