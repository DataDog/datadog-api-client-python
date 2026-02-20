"""
Get space information by display name returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.get_space_by_display_name(
        domain_name="datadog.ninja",
        space_display_name="api-test-space",
    )

    print(response)
