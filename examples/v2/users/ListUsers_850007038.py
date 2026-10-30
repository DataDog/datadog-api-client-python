"""
List all users filtered by handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# there is a valid "user" in the system
USER_DATA_ATTRIBUTES_HANDLE = environ["USER_DATA_ATTRIBUTES_HANDLE"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.list_users(
        filter_handle=USER_DATA_ATTRIBUTES_HANDLE,
    )

    print(response)
