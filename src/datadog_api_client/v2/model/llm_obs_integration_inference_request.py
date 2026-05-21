# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_anthropic_metadata import LLMObsAnthropicMetadata
    from datadog_api_client.v2.model.llm_obs_azure_open_ai_metadata import LLMObsAzureOpenAIMetadata
    from datadog_api_client.v2.model.llm_obs_bedrock_metadata import LLMObsBedrockMetadata
    from datadog_api_client.v2.model.llm_obs_inference_message import LLMObsInferenceMessage
    from datadog_api_client.v2.model.llm_obs_open_ai_metadata import LLMObsOpenAIMetadata
    from datadog_api_client.v2.model.llm_obs_inference_tool import LLMObsInferenceTool
    from datadog_api_client.v2.model.llm_obs_vertex_ai_metadata import LLMObsVertexAIMetadata


class LLMObsIntegrationInferenceRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_anthropic_metadata import LLMObsAnthropicMetadata
        from datadog_api_client.v2.model.llm_obs_azure_open_ai_metadata import LLMObsAzureOpenAIMetadata
        from datadog_api_client.v2.model.llm_obs_bedrock_metadata import LLMObsBedrockMetadata
        from datadog_api_client.v2.model.llm_obs_inference_message import LLMObsInferenceMessage
        from datadog_api_client.v2.model.llm_obs_open_ai_metadata import LLMObsOpenAIMetadata
        from datadog_api_client.v2.model.llm_obs_inference_tool import LLMObsInferenceTool
        from datadog_api_client.v2.model.llm_obs_vertex_ai_metadata import LLMObsVertexAIMetadata

        return {
            "anthropic_metadata": (LLMObsAnthropicMetadata,),
            "azure_openai_metadata": (LLMObsAzureOpenAIMetadata,),
            "bedrock_metadata": (LLMObsBedrockMetadata,),
            "frequency_penalty": (float, none_type),
            "json_schema": (str, none_type),
            "max_completion_tokens": (int, none_type),
            "max_tokens": (int, none_type),
            "messages": ([LLMObsInferenceMessage],),
            "model_id": (str,),
            "openai_metadata": (LLMObsOpenAIMetadata,),
            "presence_penalty": (float, none_type),
            "temperature": (float, none_type),
            "tools": ([LLMObsInferenceTool],),
            "top_k": (int, none_type),
            "top_p": (float, none_type),
            "vertex_ai_metadata": (LLMObsVertexAIMetadata,),
        }

    attribute_map = {
        "anthropic_metadata": "anthropic_metadata",
        "azure_openai_metadata": "azure_openai_metadata",
        "bedrock_metadata": "bedrock_metadata",
        "frequency_penalty": "frequency_penalty",
        "json_schema": "json_schema",
        "max_completion_tokens": "max_completion_tokens",
        "max_tokens": "max_tokens",
        "messages": "messages",
        "model_id": "model_id",
        "openai_metadata": "openai_metadata",
        "presence_penalty": "presence_penalty",
        "temperature": "temperature",
        "tools": "tools",
        "top_k": "top_k",
        "top_p": "top_p",
        "vertex_ai_metadata": "vertex_ai_metadata",
    }

    def __init__(
        self_,
        messages: List[LLMObsInferenceMessage],
        model_id: str,
        anthropic_metadata: Union[LLMObsAnthropicMetadata, UnsetType] = unset,
        azure_openai_metadata: Union[LLMObsAzureOpenAIMetadata, UnsetType] = unset,
        bedrock_metadata: Union[LLMObsBedrockMetadata, UnsetType] = unset,
        frequency_penalty: Union[float, none_type, UnsetType] = unset,
        json_schema: Union[str, none_type, UnsetType] = unset,
        max_completion_tokens: Union[int, none_type, UnsetType] = unset,
        max_tokens: Union[int, none_type, UnsetType] = unset,
        openai_metadata: Union[LLMObsOpenAIMetadata, UnsetType] = unset,
        presence_penalty: Union[float, none_type, UnsetType] = unset,
        temperature: Union[float, none_type, UnsetType] = unset,
        tools: Union[List[LLMObsInferenceTool], UnsetType] = unset,
        top_k: Union[int, none_type, UnsetType] = unset,
        top_p: Union[float, none_type, UnsetType] = unset,
        vertex_ai_metadata: Union[LLMObsVertexAIMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Parameters for an LLM inference request.

        :param anthropic_metadata: Anthropic-specific metadata for an inference request.
        :type anthropic_metadata: LLMObsAnthropicMetadata, optional

        :param azure_openai_metadata: Azure OpenAI-specific metadata for an integration account or inference request.
        :type azure_openai_metadata: LLMObsAzureOpenAIMetadata, optional

        :param bedrock_metadata: Amazon Bedrock-specific metadata for an inference request.
        :type bedrock_metadata: LLMObsBedrockMetadata, optional

        :param frequency_penalty: Penalty for token frequency to reduce repetition.
        :type frequency_penalty: float, none_type, optional

        :param json_schema: JSON schema for structured output, if supported by the model.
        :type json_schema: str, none_type, optional

        :param max_completion_tokens: Maximum number of completion tokens to generate (alternative to max_tokens for some providers).
        :type max_completion_tokens: int, none_type, optional

        :param max_tokens: Maximum number of tokens to generate.
        :type max_tokens: int, none_type, optional

        :param messages: List of messages in an inference conversation.
        :type messages: [LLMObsInferenceMessage]

        :param model_id: The model identifier to use for inference.
        :type model_id: str

        :param openai_metadata: OpenAI-specific metadata for an inference request.
        :type openai_metadata: LLMObsOpenAIMetadata, optional

        :param presence_penalty: Penalty for token presence to encourage topic diversity.
        :type presence_penalty: float, none_type, optional

        :param temperature: Sampling temperature between 0 and 2. Higher values produce more random output.
        :type temperature: float, none_type, optional

        :param tools: List of tools available to the model.
        :type tools: [LLMObsInferenceTool], optional

        :param top_k: Top-K sampling parameter.
        :type top_k: int, none_type, optional

        :param top_p: Nucleus sampling probability mass.
        :type top_p: float, none_type, optional

        :param vertex_ai_metadata: Vertex AI-specific metadata for an integration account or inference request.
        :type vertex_ai_metadata: LLMObsVertexAIMetadata, optional
        """
        if anthropic_metadata is not unset:
            kwargs["anthropic_metadata"] = anthropic_metadata
        if azure_openai_metadata is not unset:
            kwargs["azure_openai_metadata"] = azure_openai_metadata
        if bedrock_metadata is not unset:
            kwargs["bedrock_metadata"] = bedrock_metadata
        if frequency_penalty is not unset:
            kwargs["frequency_penalty"] = frequency_penalty
        if json_schema is not unset:
            kwargs["json_schema"] = json_schema
        if max_completion_tokens is not unset:
            kwargs["max_completion_tokens"] = max_completion_tokens
        if max_tokens is not unset:
            kwargs["max_tokens"] = max_tokens
        if openai_metadata is not unset:
            kwargs["openai_metadata"] = openai_metadata
        if presence_penalty is not unset:
            kwargs["presence_penalty"] = presence_penalty
        if temperature is not unset:
            kwargs["temperature"] = temperature
        if tools is not unset:
            kwargs["tools"] = tools
        if top_k is not unset:
            kwargs["top_k"] = top_k
        if top_p is not unset:
            kwargs["top_p"] = top_p
        if vertex_ai_metadata is not unset:
            kwargs["vertex_ai_metadata"] = vertex_ai_metadata
        super().__init__(kwargs)

        self_.messages = messages
        self_.model_id = model_id
