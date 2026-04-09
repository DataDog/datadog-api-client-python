"""
Get annotated queue interactions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

configuration = Configuration()
configuration.unstable_operations["get_llm_obs_annotated_interactions"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.get_llm_obs_annotated_interactions(
        queue_id="queue_id",
    )

    print(response)
