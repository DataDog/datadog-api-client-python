"""
Create an LLM Observability prompt returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_create_prompt_data import LLMObsCreatePromptData
from datadog_api_client.v2.model.llm_obs_create_prompt_data_attributes import LLMObsCreatePromptDataAttributes
from datadog_api_client.v2.model.llm_obs_create_prompt_request import LLMObsCreatePromptRequest
from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage
from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType

body = LLMObsCreatePromptRequest(
    data=LLMObsCreatePromptData(
        attributes=LLMObsCreatePromptDataAttributes(
            prompt_id="Example-LLM-Observability",
            title="Customer Support Assistant",
            template=[
                LLMObsPromptChatMessage(
                    content="You are a helpful customer support assistant for {{company_name}}.",
                    role="system",
                ),
                LLMObsPromptChatMessage(
                    content="Help {{customer_name}} with this question: {{question}}",
                    role="user",
                ),
            ],
        ),
        type=LLMObsPromptType.PROMPT_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_prompt"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_prompt(body=body)

    print(response)
