"""
Get a personal access token returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "personal_access_token" in the system
PERSONAL_ACCESS_TOKEN_DATA_ID = environ["PERSONAL_ACCESS_TOKEN_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.get_personal_access_token(
        pat_uuid=PERSONAL_ACCESS_TOKEN_DATA_ID,
    )

    print(response)
