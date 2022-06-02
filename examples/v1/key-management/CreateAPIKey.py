"""
Create an API key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.api_key import ApiKey

body = ApiKey(
    name="example user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_api_key(body=body)

    print(response)
