"""
Export an Agent Observability dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi

configuration = Configuration()
configuration.unstable_operations["export_llm_obs_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.export_llm_obs_dataset(
        project_id="project_id",
        dataset_id="dataset_id",
    )
