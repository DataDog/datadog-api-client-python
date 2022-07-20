"""
Edit an application key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.application_key import ApplicationKey

body = ApplicationKey(
    name="example user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_application_key(key="key", body=body)

    print(response)
