"""
Delete an Agent Observability prompt returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_prompt"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.delete_llm_obs_prompt(
        prompt_id="prompt_id",
    )

    print(response)
