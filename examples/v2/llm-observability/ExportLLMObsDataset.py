"""
Export an LLM Observability dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

configuration = Configuration()
configuration.unstable_operations["export_llm_obs_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.export_llm_obs_dataset(
        project_id="project_id",
        dataset_id="dataset_id",
    )
