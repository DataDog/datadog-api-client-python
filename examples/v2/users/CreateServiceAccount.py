"""
Create a service account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData
from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles
from datadog_api_client.v2.model.roles_type import RolesType
from datadog_api_client.v2.model.service_account_create_attributes import ServiceAccountCreateAttributes
from datadog_api_client.v2.model.service_account_create_data import ServiceAccountCreateData
from datadog_api_client.v2.model.service_account_create_request import ServiceAccountCreateRequest
from datadog_api_client.v2.model.user_relationships import UserRelationships
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = ServiceAccountCreateRequest(
    data=ServiceAccountCreateData(
        type=UsersType.USERS,
        attributes=ServiceAccountCreateAttributes(
            name="Test API Client",
            email="Example-Create_a_service_account_returns_OK_response@datadoghq.com",
            service_account=True,
        ),
        relationships=UserRelationships(
            roles=RelationshipToRoles(
                data=[
                    RelationshipToRoleData(
                        id=ROLE_DATA_ID,
                        type=RolesType.ROLES,
                    ),
                ],
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.create_service_account(body=body)

    print(response)
