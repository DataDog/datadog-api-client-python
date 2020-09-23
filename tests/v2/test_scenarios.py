# coding=utf-8
"""Test scenarios."""

import pytest
from pytest_bdd import given, scenarios

pytestmark = [
    pytest.mark.vcr,
    pytest.mark.usefixtures("ddspan"),
]


@given('there is a valid "user" in the system')
def user(context, client, unique):
    """There is a valid user in the system."""
    from datadog_api_client.v2.model import user_create_request
    from datadog_api_client.v2.model import user_create_data
    from datadog_api_client.v2.model import user_create_attributes
    from datadog_api_client.v2.model import users_type
    from datadog_api_client.v2.api.users_api import UsersApi

    api = UsersApi(client)
    body = user_create_request.UserCreateRequest(
        data=user_create_data.UserCreateData(
            type=users_type.UsersType(value="users"),
            attributes=user_create_attributes.UserCreateAttributes(
                email=str(unique) + "@datadoghq.com", ),
        ), )

    context["user"] = response = api.create_user(body=body)

    def undo():
        api.disable_user(response.data.id)

    context["undo_operations"].append(undo)


@given('there is a valid "service" in the system')
def service(context, client, unique):
    """There is a valid service in the system."""
    from datadog_api_client.v2.model import service_create_request
    from datadog_api_client.v2.model import service_create_data
    from datadog_api_client.v2.model import service_create_attributes
    from datadog_api_client.v2.model import service_type
    from datadog_api_client.v2.api.services_api import ServicesApi

    client.configuration.unstable_operations["create_service"] = True
    client.configuration.unstable_operations["delete_service"] = True
    api = ServicesApi(client)
    body = service_create_request.ServiceCreateRequest(
        data=service_create_data.ServiceCreateData(
            type=service_type.ServiceType(value="services"),
            attributes=service_create_attributes.ServiceCreateAttributes(
                name=str(unique), ),
        ), )

    response = context["service"] = api.create_service(body=body)

    def undo():
        api.delete_service(response.data.id)

    context["undo_operations"].append(undo)


@given('there is a valid "team" in the system')
def team(context, vcr_cassette, client, unique):
    """There is a valid team in the system."""
    from datadog_api_client.v2.model import team_create_request
    from datadog_api_client.v2.model import team_create_data
    from datadog_api_client.v2.model import team_create_attributes
    from datadog_api_client.v2.model import team_type
    from datadog_api_client.v2.api.teams_api import TeamsApi

    client.configuration.unstable_operations["create_team"] = True
    client.configuration.unstable_operations["delete_team"] = True
    api = TeamsApi(client)
    body = team_create_request.TeamCreateRequest(
        data=team_create_data.TeamCreateData(
            type=team_type.TeamType(value="teams"),
            attributes=team_create_attributes.TeamCreateAttributes(
                name=str(unique), ),
        ), )
    response = context["team"] = api.create_team(body=body)

    def undo():
        api.delete_team(response.data.id)

    context["undo_operations"].append(undo)


@given('there is a valid "role" in the system')
def role(context, vcr_cassette, client, unique):
    """There is a valid role in the system."""
    from datadog_api_client.v2.model import role_create_request
    from datadog_api_client.v2.model import role_create_data
    from datadog_api_client.v2.model import role_create_attributes
    from datadog_api_client.v2.model import roles_type
    from datadog_api_client.v2.api.roles_api import RolesApi

    api = RolesApi(client)
    body = role_create_request.RoleCreateRequest(
        data=role_create_data.RoleCreateData(
            type=roles_type.RolesType(value="roles"),
            attributes=role_create_attributes.RoleCreateAttributes(
                name=str(unique), ),
        ), )

    response = context["role"] = api.create_role(body=body)

    def undo():
        api.delete_role(response.data.id)

    context["undo_operations"].append(undo)


@given('there is a valid "permission" in the system')
def permission(context, client):
    """There is a valid permission in the system."""
    from datadog_api_client.v2.api.roles_api import RolesApi

    context["permission"] = RolesApi(client).list_permissions().data[0]


@given('the "permission" is granted to the "role"')
def granted_permission(context, client):
    """The permission is granted to the role."""
    from datadog_api_client.v2.model import relationship_to_permission
    from datadog_api_client.v2.model import relationship_to_permission_data
    from datadog_api_client.v2.api.roles_api import RolesApi
    role = context["role"]
    permission = context["permission"]
    api = RolesApi(client)
    body = relationship_to_permission.RelationshipToPermission(
        data=relationship_to_permission_data.RelationshipToPermissionData(
            id=permission.id,
            type=permission.type,
        ))
    api.add_permission_to_role(role.data.id, body=body)


@given('the "user" has the "role"')
def user_has_role(context, vcr_cassette, client):
    """The user has the role."""
    from datadog_api_client.v2.model import relationship_to_user
    from datadog_api_client.v2.model import relationship_to_user_data
    from datadog_api_client.v2.api.roles_api import RolesApi
    role = context["role"]
    user = context["user"]
    api = RolesApi(client)
    body = relationship_to_user.RelationshipToUser(
        data=relationship_to_user_data.RelationshipToUserData(
            id=user.data.id,
            type=user.data.type,
        ))
    api.add_user_to_role(role.data.id, body=body)

    def undo():
        api.remove_user_from_role(role.data.id, body=body)

    context["undo_operations"].append(undo)


@given('the "user" has a "user_invitation"')
def user_invitation(context, vcr_cassette, client):
    """The user has an invitation."""
    from datadog_api_client.v2.model import relationship_to_user
    from datadog_api_client.v2.model import relationship_to_user_data
    from datadog_api_client.v2.model import user_invitation_data
    from datadog_api_client.v2.model import user_invitation_relationships
    from datadog_api_client.v2.model import user_invitations_request
    from datadog_api_client.v2.model import user_invitations_type
    from datadog_api_client.v2.api.users_api import UsersApi

    user = context["user"]

    api = UsersApi(client)
    body = user_invitations_request.UserInvitationsRequest(
        data=[
            user_invitation_data.UserInvitationData(
                type=user_invitations_type.UserInvitationsType(),
                relationships=user_invitation_relationships.
                UserInvitationRelationships(
                    user=relationship_to_user.RelationshipToUser(
                        data=relationship_to_user_data.RelationshipToUserData(
                            id=user.data.id,
                            type=user.data.type,
                        ))))
        ], )
    context["user_invitation"] = api.send_invitations(body=body).data[0]


scenarios("features")
