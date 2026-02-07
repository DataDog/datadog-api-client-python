"""
Create client token returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.client_token_create_request import ClientTokenCreateRequest

body = ClientTokenCreateRequest(
    name="Example Client Token",
    origin_urls=[
        "https://example.com",
    ],
)

configuration = Configuration()
configuration.unstable_operations["create_client_token"] = True
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_client_token(body=body)

    print(response)
