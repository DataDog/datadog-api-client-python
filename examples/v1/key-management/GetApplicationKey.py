"""
Get an application key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_application_key(
        key="key",
    )

    print(response)
