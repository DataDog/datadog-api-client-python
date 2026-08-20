"""
Create a new Agent Observability prompt version returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi
from datadog_api_client.v2.model.llm_obs_create_prompt_version_data import LLMObsCreatePromptVersionData
from datadog_api_client.v2.model.llm_obs_create_prompt_version_data_attributes import (
    LLMObsCreatePromptVersionDataAttributes,
)
from datadog_api_client.v2.model.llm_obs_create_prompt_version_request import LLMObsCreatePromptVersionRequest
from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel
from datadog_api_client.v2.model.llm_obs_prompt_version_type import LLMObsPromptVersionType

body = LLMObsCreatePromptVersionRequest(
    data=LLMObsCreatePromptVersionData(
        attributes=LLMObsCreatePromptVersionDataAttributes(
            env_ids=[],
            labels=[
                LLMObsPromptVersionLabel.PRODUCTION,
            ],
            template="You are a helpful assistant for .",
        ),
        type=LLMObsPromptVersionType.PROMPT_TEMPLATE_VERSIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_prompt_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.create_llm_obs_prompt_version(prompt_id="prompt_id", body=body)

    print(response)
