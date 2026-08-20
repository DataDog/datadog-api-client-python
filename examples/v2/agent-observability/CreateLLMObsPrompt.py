"""
Create an Agent Observability prompt returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi
from datadog_api_client.v2.model.llm_obs_create_prompt_data import LLMObsCreatePromptData
from datadog_api_client.v2.model.llm_obs_create_prompt_data_attributes import LLMObsCreatePromptDataAttributes
from datadog_api_client.v2.model.llm_obs_create_prompt_request import LLMObsCreatePromptRequest
from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType
from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel

body = LLMObsCreatePromptRequest(
    data=LLMObsCreatePromptData(
        attributes=LLMObsCreatePromptDataAttributes(
            env_ids=[],
            labels=[
                LLMObsPromptVersionLabel.PRODUCTION,
            ],
            prompt_id="customer-support-assistant",
            template="You are a helpful assistant for .",
        ),
        type=LLMObsPromptType.PROMPT_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_prompt"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.create_llm_obs_prompt(body=body)

    print(response)
