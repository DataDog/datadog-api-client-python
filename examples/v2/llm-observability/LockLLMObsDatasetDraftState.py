"""
Lock LLM Observability dataset draft state returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

configuration = Configuration()
configuration.unstable_operations["lock_llm_obs_dataset_draft_state"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.lock_llm_obs_dataset_draft_state(
        project_id="project_id",
        dataset_id="dataset_id",
    )

    print(response)
