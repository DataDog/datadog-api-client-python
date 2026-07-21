"""
List LLM Observability prompts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

# there is a valid "prompt" in the system
PROMPT_DATA_ATTRIBUTES_PROMPT_ID = environ["PROMPT_DATA_ATTRIBUTES_PROMPT_ID"]

configuration = Configuration()
configuration.unstable_operations["list_llm_obs_prompts"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.list_llm_obs_prompts(
        filter_prompt_id=PROMPT_DATA_ATTRIBUTES_PROMPT_ID,
    )

    print(response)
