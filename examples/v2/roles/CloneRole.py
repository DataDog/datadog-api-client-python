"""
Create a new role by cloning an existing role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.role_clone import RoleClone
from datadog_api_client.v2.model.role_clone_attributes import RoleCloneAttributes
from datadog_api_client.v2.model.role_clone_request import RoleCloneRequest
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RoleCloneRequest(
    data=RoleClone(
        attributes=RoleCloneAttributes(
            name="Example-Create_a_new_role_by_cloning_an_existing_role_returns_OK_response clone",
        ),
        type=RolesType.ROLES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.clone_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
