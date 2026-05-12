"""
Update current user returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.user_update_attributes import UserUpdateAttributes
from datadog_api_client.v2.model.user_update_data import UserUpdateData
from datadog_api_client.v2.model.user_update_request import UserUpdateRequest
from datadog_api_client.v2.model.users_type import UsersType

body = UserUpdateRequest(
    data=UserUpdateData(
        attributes=UserUpdateAttributes(
            title=None,
        ),
        id="00000000-0000-feed-0000-000000000000",
        type=UsersType.USERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.update_current_user(body=body)

    print(response)
