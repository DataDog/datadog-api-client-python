"""
Update a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.permissions_type import PermissionsType
from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData
from datadog_api_client.v2.model.relationship_to_permissions import RelationshipToPermissions
from datadog_api_client.v2.model.role_relationships import RoleRelationships
from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes
from datadog_api_client.v2.model.role_update_data import RoleUpdateData
from datadog_api_client.v2.model.role_update_request import RoleUpdateRequest
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = environ["ROLE_DATA_ATTRIBUTES_NAME"]
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RoleUpdateRequest(
    data=RoleUpdateData(
        id=ROLE_DATA_ID,
        type=RolesType.ROLES,
        attributes=RoleUpdateAttributes(
            name="developers-updated",
        ),
        relationships=RoleRelationships(
            permissions=RelationshipToPermissions(
                data=[
                    RelationshipToPermissionData(
                        id=PERMISSION_ID,
                        type=PermissionsType.PERMISSIONS,
                    ),
                ],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.update_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
