"""
Create an API key returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.api_key_create_attributes import APIKeyCreateAttributes
from datadog_api_client.v2.model.api_key_create_data import APIKeyCreateData
from datadog_api_client.v2.model.api_key_create_request import APIKeyCreateRequest
from datadog_api_client.v2.model.api_keys_type import APIKeysType

body = APIKeyCreateRequest(
    data=APIKeyCreateData(
        type=APIKeysType.API_KEYS,
        attributes=APIKeyCreateAttributes(
            name="Example-Create_an_API_key_returns_Created_response",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_api_key(body=body)

    print(response)
