"""
Delete an application key owned by current user returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    api_instance.delete_current_user_application_key(
        app_key_id="app_key_id",
    )
