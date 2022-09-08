"""
Update a user returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.user_update_attributes import UserUpdateAttributes
from datadog_api_client.v2.model.user_update_data import UserUpdateData
from datadog_api_client.v2.model.user_update_request import UserUpdateRequest
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserUpdateRequest(
    data=UserUpdateData(
        id=USER_DATA_ID,
        type=UsersType.USERS,
        attributes=UserUpdateAttributes(
            name="updated",
            disabled=True,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.update_user(user_id=USER_DATA_ID, body=body)

    print(response)
