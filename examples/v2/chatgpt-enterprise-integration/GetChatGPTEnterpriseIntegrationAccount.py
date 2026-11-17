"""
Get a ChatGPT Enterprise integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.chat_gpt_enterprise_integration_api import ChatGPTEnterpriseIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_chat_gpt_enterprise_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChatGPTEnterpriseIntegrationApi(api_client)
    response = api_instance.get_chat_gpt_enterprise_integration_account(
        account_id="account_id",
    )

    print(response)
