"""
Delete a Google Chat organization binding returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    api_instance.delete_google_chat_organization(
        organization_binding_id="organization_binding_id",
    )
