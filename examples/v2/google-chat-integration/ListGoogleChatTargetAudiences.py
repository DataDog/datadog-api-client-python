"""
Get all target audiences returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.list_google_chat_target_audiences(
        organization_binding_id="organization_binding_id",
    )

    print(response)
