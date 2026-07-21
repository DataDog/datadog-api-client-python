"""
Update an LLM Observability prompt returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType
from datadog_api_client.v2.model.llm_obs_update_prompt_data import LLMObsUpdatePromptData
from datadog_api_client.v2.model.llm_obs_update_prompt_data_attributes import LLMObsUpdatePromptDataAttributes
from datadog_api_client.v2.model.llm_obs_update_prompt_request import LLMObsUpdatePromptRequest

# there is a valid "prompt" in the system
PROMPT_DATA_ATTRIBUTES_PROMPT_ID = environ["PROMPT_DATA_ATTRIBUTES_PROMPT_ID"]

body = LLMObsUpdatePromptRequest(
    data=LLMObsUpdatePromptData(
        attributes=LLMObsUpdatePromptDataAttributes(
            title="Customer Support Assistant",
        ),
        type=LLMObsPromptType.PROMPT_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_prompt"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.update_llm_obs_prompt(prompt_id=PROMPT_DATA_ATTRIBUTES_PROMPT_ID, body=body)

    print(response)
