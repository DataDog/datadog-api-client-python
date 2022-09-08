"""
Grant permission to a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.permissions_type import PermissionsType
from datadog_api_client.v2.model.relationship_to_permission import RelationshipToPermission
from datadog_api_client.v2.model.relationship_to_permission_data import RelationshipToPermissionData

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RelationshipToPermission(
    data=RelationshipToPermissionData(
        id=PERMISSION_ID,
        type=PermissionsType.PERMISSIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.add_permission_to_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
