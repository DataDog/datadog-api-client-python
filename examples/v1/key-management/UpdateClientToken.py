"""
Update client token returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.key_management_api import KeyManagementApi
from datadog_api_client.v1.model.client_token_update_request import ClientTokenUpdateRequest

body = ClientTokenUpdateRequest(
    hash="1234567890abcdef1234567890abcdef123",
    name="Updated Client Token Name",
    origin_urls=[
        "https://example.com",
    ],
)

configuration = Configuration()
configuration.unstable_operations["update_client_token"] = True
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_client_token(body=body)

    print(response)
