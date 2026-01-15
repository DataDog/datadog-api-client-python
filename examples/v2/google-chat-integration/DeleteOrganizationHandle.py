"""
Delete organization handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi

# there is a valid "organization_handle" in the system
ORGANIZATION_HANDLE_DATA_ID = environ["ORGANIZATION_HANDLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    api_instance.delete_organization_handle(
        organization_binding_id="e54cb570-c674-529c-769d-84b312288ed7",
        handle_id=ORGANIZATION_HANDLE_DATA_ID,
    )
