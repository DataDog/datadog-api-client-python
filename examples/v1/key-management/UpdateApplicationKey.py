"""
Edit an application key returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.application_key import ApplicationKey

body = ApplicationKey(hash="1234512345123459cda4eb9ced49a3d84fd0138c", name="example user", owner="example.com")

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_application_key(key="key", body=body)

    print(response)
