"""
Create a user returns "User created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.users_api import UsersApi
from datadog_api_client.v1.model.access_role import AccessRole
from datadog_api_client.v1.model.user import User

body = User(
    access_role=AccessRole.STANDARD,
    disabled=False,
    email="test@datadoghq.com",
    handle="test@datadoghq.com",
    name="test user",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.create_user(body=body)

    print(response)
