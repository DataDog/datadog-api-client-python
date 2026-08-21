"""
Update an Agent Observability prompt returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi
from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType
from datadog_api_client.v2.model.llm_obs_update_prompt_data import LLMObsUpdatePromptData
from datadog_api_client.v2.model.llm_obs_update_prompt_data_attributes import LLMObsUpdatePromptDataAttributes
from datadog_api_client.v2.model.llm_obs_update_prompt_request import LLMObsUpdatePromptRequest

body = LLMObsUpdatePromptRequest(
    data=LLMObsUpdatePromptData(
        attributes=LLMObsUpdatePromptDataAttributes(),
        type=LLMObsPromptType.PROMPT_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_prompt"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.update_llm_obs_prompt(prompt_id="prompt_id", body=body)

    print(response)
