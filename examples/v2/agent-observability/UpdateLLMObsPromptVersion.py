"""
Update an Agent Observability prompt version returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi
from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel
from datadog_api_client.v2.model.llm_obs_prompt_version_type import LLMObsPromptVersionType
from datadog_api_client.v2.model.llm_obs_update_prompt_version_data import LLMObsUpdatePromptVersionData
from datadog_api_client.v2.model.llm_obs_update_prompt_version_data_attributes import (
    LLMObsUpdatePromptVersionDataAttributes,
)
from datadog_api_client.v2.model.llm_obs_update_prompt_version_request import LLMObsUpdatePromptVersionRequest

body = LLMObsUpdatePromptVersionRequest(
    data=LLMObsUpdatePromptVersionData(
        attributes=LLMObsUpdatePromptVersionDataAttributes(
            env_ids=[],
            labels=[
                LLMObsPromptVersionLabel.PRODUCTION,
            ],
        ),
        type=LLMObsPromptVersionType.PROMPT_TEMPLATE_VERSIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_prompt_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.update_llm_obs_prompt_version(prompt_id="prompt_id", version=9223372036854775807, body=body)

    print(response)
