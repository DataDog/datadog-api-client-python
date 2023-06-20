"""
Update a role returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.role_update_request import RoleUpdateRequestJSON

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = environ["ROLE_DATA_ATTRIBUTES_NAME"]
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RoleUpdateRequestJSON(
    name="developers-updated",
    permissions=["f2a8beb4-91f8-962d-b6d9-60215cda2214"],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.update_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
