"""
Get patterns run status returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi

configuration = Configuration()
configuration.unstable_operations["get_llm_obs_patterns_run_status"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.get_llm_obs_patterns_run_status(
        config_id="config_id",
    )

    print(response)
