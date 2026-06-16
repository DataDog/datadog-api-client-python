"""
Get the delegated user returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.get_google_chat_delegated_user(
        organization_binding_id="organization_binding_id",
    )

    print(response)
