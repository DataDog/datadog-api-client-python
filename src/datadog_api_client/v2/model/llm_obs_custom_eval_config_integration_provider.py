# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsCustomEvalConfigIntegrationProvider(ModelSimple):
    """
    Name of the LLM integration provider.

    :param value: Must be one of ["openai", "amazon-bedrock", "anthropic", "azure-openai", "vertex-ai", "llm-proxy"].
    :type value: str
    """

    allowed_values = {
        "openai",
        "amazon-bedrock",
        "anthropic",
        "azure-openai",
        "vertex-ai",
        "llm-proxy",
    }
    OPENAI: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    AMAZON_BEDROCK: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    ANTHROPIC: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    AZURE_OPENAI: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    VERTEX_AI: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    LLM_PROXY: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsCustomEvalConfigIntegrationProvider.OPENAI = LLMObsCustomEvalConfigIntegrationProvider("openai")
LLMObsCustomEvalConfigIntegrationProvider.AMAZON_BEDROCK = LLMObsCustomEvalConfigIntegrationProvider("amazon-bedrock")
LLMObsCustomEvalConfigIntegrationProvider.ANTHROPIC = LLMObsCustomEvalConfigIntegrationProvider("anthropic")
LLMObsCustomEvalConfigIntegrationProvider.AZURE_OPENAI = LLMObsCustomEvalConfigIntegrationProvider("azure-openai")
LLMObsCustomEvalConfigIntegrationProvider.VERTEX_AI = LLMObsCustomEvalConfigIntegrationProvider("vertex-ai")
LLMObsCustomEvalConfigIntegrationProvider.LLM_PROXY = LLMObsCustomEvalConfigIntegrationProvider("llm-proxy")
