"""
Create a user returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.user_create_attributes import UserCreateAttributes
from datadog_api_client.v2.model.user_create_data import UserCreateData
from datadog_api_client.v2.model.user_create_request import UserCreateRequest
from datadog_api_client.v2.model.users_type import UsersType

body = UserCreateRequest(
    data=UserCreateData(
        type=UsersType.USERS,
        attributes=UserCreateAttributes(
            name="Datadog API Client Python",
            email="Example-Create_a_user_returns_OK_response@datadoghq.com",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.create_user(body=body)

    print(response)
