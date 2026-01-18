"""
Get all organization handles returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.list_organization_handles(
        organization_binding_id="e54cb570-c674-529c-769d-84b312288ed7",
    )

    print(response)
