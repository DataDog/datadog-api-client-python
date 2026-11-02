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
    Name of the LLM integration provider. Use `deterministic` for a code evaluator, which runs `llm_judge_config.user_specified_json_post_processing_function` instead of calling an LLM. `insights_sponsored` is returned for evaluators that Datadog manages and cannot be set.

    :param value: Must be one of ["openai", "amazon_bedrock", "anthropic", "azure_openai", "vertex_ai", "llmproxy", "deterministic", "typesafe", "datadog", "datadog_ai_gateway", "insights_sponsored"].
    :type value: str
    """

    allowed_values = {
        "openai",
        "amazon_bedrock",
        "anthropic",
        "azure_openai",
        "vertex_ai",
        "llmproxy",
        "deterministic",
        "typesafe",
        "datadog",
        "datadog_ai_gateway",
        "insights_sponsored",
    }
    OPENAI: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    AMAZON_BEDROCK: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    ANTHROPIC: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    AZURE_OPENAI: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    VERTEX_AI: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    LLM_PROXY: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    DETERMINISTIC: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    TYPESAFE: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    DATADOG: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    DATADOG_AI_GATEWAY: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]
    INSIGHTS_SPONSORED: ClassVar["LLMObsCustomEvalConfigIntegrationProvider"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsCustomEvalConfigIntegrationProvider.OPENAI = LLMObsCustomEvalConfigIntegrationProvider("openai")
LLMObsCustomEvalConfigIntegrationProvider.AMAZON_BEDROCK = LLMObsCustomEvalConfigIntegrationProvider("amazon_bedrock")
LLMObsCustomEvalConfigIntegrationProvider.ANTHROPIC = LLMObsCustomEvalConfigIntegrationProvider("anthropic")
LLMObsCustomEvalConfigIntegrationProvider.AZURE_OPENAI = LLMObsCustomEvalConfigIntegrationProvider("azure_openai")
LLMObsCustomEvalConfigIntegrationProvider.VERTEX_AI = LLMObsCustomEvalConfigIntegrationProvider("vertex_ai")
LLMObsCustomEvalConfigIntegrationProvider.LLM_PROXY = LLMObsCustomEvalConfigIntegrationProvider("llmproxy")
LLMObsCustomEvalConfigIntegrationProvider.DETERMINISTIC = LLMObsCustomEvalConfigIntegrationProvider("deterministic")
LLMObsCustomEvalConfigIntegrationProvider.TYPESAFE = LLMObsCustomEvalConfigIntegrationProvider("typesafe")
LLMObsCustomEvalConfigIntegrationProvider.DATADOG = LLMObsCustomEvalConfigIntegrationProvider("datadog")
LLMObsCustomEvalConfigIntegrationProvider.DATADOG_AI_GATEWAY = LLMObsCustomEvalConfigIntegrationProvider(
    "datadog_ai_gateway"
)
LLMObsCustomEvalConfigIntegrationProvider.INSIGHTS_SPONSORED = LLMObsCustomEvalConfigIntegrationProvider(
    "insights_sponsored"
)
