"""
Send invitation emails returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData
from datadog_api_client.v2.model.user_invitation_data import UserInvitationData
from datadog_api_client.v2.model.user_invitation_relationships import UserInvitationRelationships
from datadog_api_client.v2.model.user_invitations_request import UserInvitationsRequest
from datadog_api_client.v2.model.user_invitations_type import UserInvitationsType
from datadog_api_client.v2.model.users_type import UsersType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = UserInvitationsRequest(
    data=[
        UserInvitationData(
            type=UserInvitationsType.USER_INVITATIONS,
            relationships=UserInvitationRelationships(
                user=RelationshipToUser(
                    data=RelationshipToUserData(
                        type=UsersType.USERS,
                        id=USER_DATA_ID,
                    ),
                ),
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    response = api_instance.send_invitations(body=body)

    print(response)
