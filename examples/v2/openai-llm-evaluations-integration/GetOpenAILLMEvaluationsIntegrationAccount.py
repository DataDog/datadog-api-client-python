"""
Get an OpenAI LLM Evaluations account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_aillm_evaluations_integration_api import OpenAILLMEvaluationsIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_open_aillm_evaluations_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAILLMEvaluationsIntegrationApi(api_client)
    response = api_instance.get_open_aillm_evaluations_integration_account(
        account_id="account_id",
    )

    print(response)
