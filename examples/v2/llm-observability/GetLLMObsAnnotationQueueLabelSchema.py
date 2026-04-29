"""
Get annotation queue label schema returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

configuration = Configuration()
configuration.unstable_operations["get_llm_obs_annotation_queue_label_schema"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.get_llm_obs_annotation_queue_label_schema(
        queue_id="queue_id",
    )

    print(response)
