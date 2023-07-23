"""
Create a user returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.user_create_request import UserCreateRequestJSON

body = UserCreateRequestJSON(
    name="Datadog API Client Python",
    email="Example-User@datadoghq.com",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.create_user(body=body)

    print(response)
