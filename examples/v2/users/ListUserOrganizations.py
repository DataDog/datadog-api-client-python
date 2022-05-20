"""
Get a user organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.list_user_organizations(
        user_id="00000000-0000-9999-0000-000000000000",
    )

    print(response)
