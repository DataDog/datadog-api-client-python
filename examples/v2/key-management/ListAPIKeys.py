"""
Get all API keys returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "api_key" in the system
API_KEY_DATA_ATTRIBUTES_NAME = environ["API_KEY_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.list_api_keys(
        filter=API_KEY_DATA_ATTRIBUTES_NAME,
    )

    print(response)
