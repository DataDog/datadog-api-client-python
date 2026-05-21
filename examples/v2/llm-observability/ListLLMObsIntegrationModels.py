"""
List LLM integration models returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_integration_name import LLMObsIntegrationName

configuration = Configuration()
configuration.unstable_operations["list_llm_obs_integration_models"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.list_llm_obs_integration_models(
        integration=LLMObsIntegrationName.OPENAI,
        account_id="account_id",
    )

    print(response)
