"""
Revoke permission returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.relationship_to_permission import RelationshipToPermissionJSON

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "permission" in the system
PERMISSION_ID = environ["PERMISSION_ID"]

body = RelationshipToPermissionJSON(
    id=PERMISSION_ID,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.remove_permission_from_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
