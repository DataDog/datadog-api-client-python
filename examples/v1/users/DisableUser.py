"""
Disable a user returns "User disabled" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.disable_user(
        user_handle="test@datadoghq.com",
    )

    print(response)
