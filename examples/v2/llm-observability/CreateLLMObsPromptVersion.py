"""
Create a new LLM Observability prompt version returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_create_prompt_version_data import LLMObsCreatePromptVersionData
from datadog_api_client.v2.model.llm_obs_create_prompt_version_data_attributes import (
    LLMObsCreatePromptVersionDataAttributes,
)
from datadog_api_client.v2.model.llm_obs_create_prompt_version_request import LLMObsCreatePromptVersionRequest
from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage
from datadog_api_client.v2.model.llm_obs_prompt_version_type import LLMObsPromptVersionType

# there is a valid "prompt" in the system
PROMPT_DATA_ATTRIBUTES_PROMPT_ID = environ["PROMPT_DATA_ATTRIBUTES_PROMPT_ID"]

body = LLMObsCreatePromptVersionRequest(
    data=LLMObsCreatePromptVersionData(
        attributes=LLMObsCreatePromptVersionDataAttributes(
            template=[
                LLMObsPromptChatMessage(
                    content="You are a concise customer support assistant for {{company_name}}.",
                    role="system",
                ),
                LLMObsPromptChatMessage(
                    content="Answer {{customer_name}}'s question: {{question}}",
                    role="user",
                ),
            ],
        ),
        type=LLMObsPromptVersionType.PROMPT_TEMPLATE_VERSIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_prompt_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_prompt_version(prompt_id=PROMPT_DATA_ATTRIBUTES_PROMPT_ID, body=body)

    print(response)
