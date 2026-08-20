"""
Get annotated interactions by content IDs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi

configuration = Configuration()
configuration.unstable_operations["get_llm_obs_annotated_interactions_by_trace_i_ds"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.get_llm_obs_annotated_interactions_by_trace_i_ds(
        content_ids=[],
    )

    print(response)
