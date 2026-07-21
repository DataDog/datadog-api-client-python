"""
Delete an LLM Observability prompt returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

# there is a valid "prompt" in the system
PROMPT_DATA_ATTRIBUTES_PROMPT_ID = environ["PROMPT_DATA_ATTRIBUTES_PROMPT_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_prompt"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.delete_llm_obs_prompt(
        prompt_id=PROMPT_DATA_ATTRIBUTES_PROMPT_ID,
    )

    print(response)
