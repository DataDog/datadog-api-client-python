"""
Remove a user from a role returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = RelationshipToUser(
    data=RelationshipToUserData(
        id=USER_DATA_ID,
        type=UsersType.USERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.remove_user_from_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
