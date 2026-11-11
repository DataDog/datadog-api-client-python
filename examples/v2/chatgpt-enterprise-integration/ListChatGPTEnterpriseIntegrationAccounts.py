"""
List ChatGPT Enterprise integration accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.chat_gpt_enterprise_integration_api import ChatGPTEnterpriseIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_chat_gpt_enterprise_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChatGPTEnterpriseIntegrationApi(api_client)
    response = api_instance.list_chat_gpt_enterprise_integration_accounts()

    print(response)
