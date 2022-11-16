"""
Edit an API key returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.api_key_update_attributes import APIKeyUpdateAttributes
from datadog_api_client.v2.model.api_key_update_data import APIKeyUpdateData
from datadog_api_client.v2.model.api_key_update_request import APIKeyUpdateRequest
from datadog_api_client.v2.model.api_keys_type import APIKeysType

# there is a valid "api_key" in the system
API_KEY_DATA_ID = environ["API_KEY_DATA_ID"]

body = APIKeyUpdateRequest(
    data=APIKeyUpdateData(
        type=APIKeysType.API_KEYS,
        id=API_KEY_DATA_ID,
        attributes=APIKeyUpdateAttributes(
            name="Example-Edit_an_API_key_returns_OK_response",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.update_api_key(api_key_id=API_KEY_DATA_ID, body=body)

    print(response)
