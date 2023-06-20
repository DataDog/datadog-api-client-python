"""
Update a user returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.user_update_request import UserUpdateRequestJSON

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserUpdateRequestJSON(
    name="updated",
    disabled=True,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.update_user(user_id=USER_DATA_ID, body=body)

    print(response)
