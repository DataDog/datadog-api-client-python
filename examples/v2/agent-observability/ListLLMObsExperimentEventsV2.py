"""
List Agent Observability experiment events (v2) returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi

configuration = Configuration()
configuration.unstable_operations["list_llm_obs_experiment_events_v2"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.list_llm_obs_experiment_events_v2(
        experiment_id="experiment_id",
    )

    print(response)
