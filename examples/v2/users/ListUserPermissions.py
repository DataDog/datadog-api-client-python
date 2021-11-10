"""
Get a user permissions returns "OK" response
"""

from os import environ
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

with ApiClient(Configuration()) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.list_user_permissions(user_id=USER_DATA_ID)

    print(response)
