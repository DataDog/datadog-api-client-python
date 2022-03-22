"""
Edit an API key returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.api_key import ApiKey

body = ApiKey(
    created="2019-08-02 15:31:07",
    created_by="john@example.com",
    key="1234512345123456abcabc912349abcd",
    name="example user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_api_key(key="key", body=body)

    print(response)
