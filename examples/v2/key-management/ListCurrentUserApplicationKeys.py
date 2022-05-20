"""
Get all application keys owned by current user returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_current_user_application_keys()

    print(response)
