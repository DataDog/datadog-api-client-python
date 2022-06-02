"""
Get API key returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "api_key" in the system
API_KEY_DATA_ID = environ["API_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_api_key(
        api_key_id=API_KEY_DATA_ID,
    )

    print(response)
