"""
List personal access tokens returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

configuration = Configuration()
configuration.unstable_operations["list_personal_access_tokens"] = True
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_personal_access_tokens()

    print(response)
