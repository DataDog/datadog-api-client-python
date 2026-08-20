"""
List LLM integration accounts returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agent_observability_api import AgentObservabilityApi
from datadog_api_client.v2.model.llm_obs_integration_name import LLMObsIntegrationName

configuration = Configuration()
configuration.unstable_operations["list_llm_obs_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = AgentObservabilityApi(api_client)
    response = api_instance.list_llm_obs_integration_accounts(
        integration=LLMObsIntegrationName.OPENAI,
    )

    print(response)
