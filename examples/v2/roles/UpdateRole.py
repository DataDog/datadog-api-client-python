"""
Update a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes
from datadog_api_client.v2.model.role_update_data import RoleUpdateData
from datadog_api_client.v2.model.role_update_request import RoleUpdateRequest
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = environ["ROLE_DATA_ATTRIBUTES_NAME"]
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = RoleUpdateRequest(
    data=RoleUpdateData(
        id=ROLE_DATA_ID,
        type=RolesType("roles"),
        attributes=RoleUpdateAttributes(
            name="developers-updated",
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.update_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
