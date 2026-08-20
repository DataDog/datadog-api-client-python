"""
Get a specific Agent Observability prompt version returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi

configuration = Configuration()
configuration.unstable_operations["get_llm_obs_prompt_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.get_llm_obs_prompt_version(
        prompt_id="prompt_id",
        version=9223372036854775807,
    )

    print(response)
