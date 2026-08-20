"""
Delete a patterns configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_patterns_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    api_instance.delete_llm_obs_patterns_config(
        config_id="config_id",
    )
