"""
Create role returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.role_create_request import RoleCreateRequestJSON

body = RoleCreateRequestJSON(
    name="Example-Role",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.create_role(body=body)

    print(response)
