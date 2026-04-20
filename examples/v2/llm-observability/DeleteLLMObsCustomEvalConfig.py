"""
Delete a custom evaluator configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_custom_eval_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.delete_llm_obs_custom_eval_config(
        eval_name="eval_name",
    )
