"""
Get user details returns "OK for get user" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.get_user(
        user_handle="test@datadoghq.com",
    )

    print(response)
