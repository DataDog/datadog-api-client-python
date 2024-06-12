"""
Create role with a permission returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.permissions_type import PermissionsType
from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData
from datadog_api_client.v2.model.relationship_to_permissions import RelationshipToPermissions
from datadog_api_client.v2.model.role_create_attributes import RoleCreateAttributes
from datadog_api_client.v2.model.role_create_data import RoleCreateData
from datadog_api_client.v2.model.role_create_request import RoleCreateRequest
from datadog_api_client.v2.model.role_relationships import RoleRelationships
from datadog_api_client.v2.model.roles_type import RolesType

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RoleCreateRequest(
    data=RoleCreateData(
        type=RolesType.ROLES,
        attributes=RoleCreateAttributes(
            name="Example-Role",
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
    response = api_instance.create_role(body=body)

    print(response)
