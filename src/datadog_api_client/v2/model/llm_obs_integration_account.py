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
    from datadog_api_client.v2.model.llm_obs_azure_open_ai_metadata import LLMObsAzureOpenAIMetadata
    from datadog_api_client.v2.model.llm_obs_vertex_ai_metadata import LLMObsVertexAIMetadata


class LLMObsIntegrationAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_azure_open_ai_metadata import LLMObsAzureOpenAIMetadata
        from datadog_api_client.v2.model.llm_obs_vertex_ai_metadata import LLMObsVertexAIMetadata

        return {
            "account_id": (str,),
            "account_name": (str,),
            "account_region": (str,),
            "azure_openai_metadata": (LLMObsAzureOpenAIMetadata,),
            "id": (str,),
            "integration": (str,),
            "vertex_ai_metadata": (LLMObsVertexAIMetadata,),
        }

    attribute_map = {
        "account_id": "account_id",
        "account_name": "account_name",
        "account_region": "account_region",
        "azure_openai_metadata": "azure_openai_metadata",
        "id": "id",
        "integration": "integration",
        "vertex_ai_metadata": "vertex_ai_metadata",
    }

    def __init__(
        self_,
        account_id: str,
        account_name: str,
        id: str,
        integration: str,
        account_region: Union[str, UnsetType] = unset,
        azure_openai_metadata: Union[LLMObsAzureOpenAIMetadata, UnsetType] = unset,
        vertex_ai_metadata: Union[LLMObsVertexAIMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        A configured account for an LLM provider integration.

        :param account_id: Provider-specific account identifier.
        :type account_id: str

        :param account_name: Human-readable name for the integration account.
        :type account_name: str

        :param account_region: Provider region associated with the account, if applicable.
        :type account_region: str, optional

        :param azure_openai_metadata: Azure OpenAI-specific metadata for an integration account or inference request.
        :type azure_openai_metadata: LLMObsAzureOpenAIMetadata, optional

        :param id: Unique identifier for the integration account.
        :type id: str

        :param integration: The name of the LLM provider integration.
        :type integration: str

        :param vertex_ai_metadata: Vertex AI-specific metadata for an integration account or inference request.
        :type vertex_ai_metadata: LLMObsVertexAIMetadata, optional
        """
        if account_region is not unset:
            kwargs["account_region"] = account_region
        if azure_openai_metadata is not unset:
            kwargs["azure_openai_metadata"] = azure_openai_metadata
        if vertex_ai_metadata is not unset:
            kwargs["vertex_ai_metadata"] = vertex_ai_metadata
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.account_name = account_name
        self_.id = id
        self_.integration = integration
