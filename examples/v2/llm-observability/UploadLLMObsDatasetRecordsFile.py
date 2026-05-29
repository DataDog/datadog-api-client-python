"""
Upload records to an LLM Observability dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

configuration = Configuration()
configuration.unstable_operations["upload_llm_obs_dataset_records_file"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.upload_llm_obs_dataset_records_file(
        project_id="project_id",
        dataset_id="dataset_id",
    )
