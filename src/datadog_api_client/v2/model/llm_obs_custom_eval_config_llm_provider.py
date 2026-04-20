# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_bedrock_options import (
        LLMObsCustomEvalConfigBedrockOptions,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_integration_provider import (
        LLMObsCustomEvalConfigIntegrationProvider,
    )
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_vertex_ai_options import (
        LLMObsCustomEvalConfigVertexAIOptions,
    )


class LLMObsCustomEvalConfigLLMProvider(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_bedrock_options import (
            LLMObsCustomEvalConfigBedrockOptions,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_integration_provider import (
            LLMObsCustomEvalConfigIntegrationProvider,
        )
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_vertex_ai_options import (
            LLMObsCustomEvalConfigVertexAIOptions,
        )

        return {
            "bedrock": (LLMObsCustomEvalConfigBedrockOptions,),
            "integration_account_id": (str,),
            "integration_provider": (LLMObsCustomEvalConfigIntegrationProvider,),
            "model_name": (str,),
            "vertex_ai": (LLMObsCustomEvalConfigVertexAIOptions,),
        }

    attribute_map = {
        "bedrock": "bedrock",
        "integration_account_id": "integration_account_id",
        "integration_provider": "integration_provider",
        "model_name": "model_name",
        "vertex_ai": "vertex_ai",
    }

    def __init__(
        self_,
        bedrock: Union[LLMObsCustomEvalConfigBedrockOptions, UnsetType] = unset,
        integration_account_id: Union[str, UnsetType] = unset,
        integration_provider: Union[LLMObsCustomEvalConfigIntegrationProvider, UnsetType] = unset,
        model_name: Union[str, UnsetType] = unset,
        vertex_ai: Union[LLMObsCustomEvalConfigVertexAIOptions, UnsetType] = unset,
        **kwargs,
    ):
        """
        LLM provider configuration for a custom evaluator.

        :param bedrock: AWS Bedrock-specific options for LLM provider configuration.
        :type bedrock: LLMObsCustomEvalConfigBedrockOptions, optional

        :param integration_account_id: Integration account identifier.
        :type integration_account_id: str, optional

        :param integration_provider: Name of the LLM integration provider.
        :type integration_provider: LLMObsCustomEvalConfigIntegrationProvider, optional

        :param model_name: Name of the LLM model.
        :type model_name: str, optional

        :param vertex_ai: Google Vertex AI-specific options for LLM provider configuration.
        :type vertex_ai: LLMObsCustomEvalConfigVertexAIOptions, optional
        """
        if bedrock is not unset:
            kwargs["bedrock"] = bedrock
        if integration_account_id is not unset:
            kwargs["integration_account_id"] = integration_account_id
        if integration_provider is not unset:
            kwargs["integration_provider"] = integration_provider
        if model_name is not unset:
            kwargs["model_name"] = model_name
        if vertex_ai is not unset:
            kwargs["vertex_ai"] = vertex_ai
        super().__init__(kwargs)
