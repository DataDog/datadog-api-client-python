"""
Add a user to a role returns "OK" response
"""

from os import environ
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = RelationshipToUser(
    data=RelationshipToUserData(id="acdbf151-4b02-7d24-bb34-66d6994071a7", type=UsersType("users"))
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.add_user_to_role(role_id=ROLE_DATA_ID, body=body)

    print(response)
