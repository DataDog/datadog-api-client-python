"""
Get all Google Chat organization bindings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.list_google_chat_organizations()

    print(response)
