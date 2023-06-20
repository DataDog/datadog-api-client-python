"""
Create an API key returns "Created" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.api_key_create_request import APIKeyCreateRequestJSON

body = APIKeyCreateRequestJSON(
    name="Example-Key-Management",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_api_key(body=body)

    print(response)
