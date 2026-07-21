"""
Get a specific LLM Observability prompt version returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

# there is a valid "prompt" in the system
PROMPT_DATA_ATTRIBUTES_PROMPT_ID = environ["PROMPT_DATA_ATTRIBUTES_PROMPT_ID"]

# there is a valid "prompt_version" in the system
PROMPT_VERSION_DATA_ATTRIBUTES_VERSION = environ["PROMPT_VERSION_DATA_ATTRIBUTES_VERSION"]

configuration = Configuration()
configuration.unstable_operations["get_llm_obs_prompt_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.get_llm_obs_prompt_version(
        prompt_id=PROMPT_DATA_ATTRIBUTES_PROMPT_ID,
        version=int(PROMPT_VERSION_DATA_ATTRIBUTES_VERSION),
    )

    print(response)
