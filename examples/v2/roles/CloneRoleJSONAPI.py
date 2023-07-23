"""
Create a new role by cloning an existing role returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.role_clone_request import RoleCloneRequestJSON

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RoleCloneRequestJSON(
    name="Example-Role clone",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.clone_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
