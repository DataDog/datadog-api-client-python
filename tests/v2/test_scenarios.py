# coding=utf-8
"""Test scenarios."""

import warnings

import pytest
from pytest_bdd import given, scenarios

pytestmark = [
    pytest.mark.vcr,
    pytest.mark.usefixtures("ddspan"),
]


@given('there is a valid "user" in the system')
def user(vcr_cassette, client, unique):
    """There is a valid user in the system."""
    from datadog_api_client.v2.exceptions import ApiException
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
                email=str(unique) + "@datadoghq.com",
            ),
        ),
    )
    response = api.create_user(body=body)
    yield response
    if vcr_cassette.record_mode != "none":
        number_of_interactions = len(vcr_cassette.data)
        try:
            api.disable_user(response.data.id)
        except ApiException as e:
            warnings.warn(str(e))
        vcr_cassette.data = vcr_cassette.data[:number_of_interactions]


@given('there is a valid "role" in the system')
def role(vcr_cassette, client, unique):
    """There is a valid role in the system."""
    from datadog_api_client.v2.exceptions import ApiException
    from datadog_api_client.v2.model import role_create_request
    from datadog_api_client.v2.model import role_create_data
    from datadog_api_client.v2.model import role_create_attributes
    from datadog_api_client.v2.model import roles_type
    from datadog_api_client.v2.api.roles_api import RolesApi

    api = RolesApi(client)
    body = role_create_request.RoleCreateRequest(
        data=role_create_data.RoleCreateData(
            type=roles_type.RolesType(value="roles"),
            attributes=role_create_attributes.RoleCreateAttributes(name=str(unique),),
        ),
    )
    response = api.create_role(body=body)
    yield response
    if vcr_cassette.record_mode != "none":
        number_of_interactions = len(vcr_cassette.data)
        try:
            api.delete_role(response.data.id)
        except ApiException as e:
            warnings.warn(str(e))
        vcr_cassette.data = vcr_cassette.data[:number_of_interactions]


@given('there is a valid "permission" in the system')
def permission(client):
    """There is a valid permission in the system."""
    from datadog_api_client.v2.api.roles_api import RolesApi

    return RolesApi(client).list_permissions().data[0]


@given('the "permission" is granted to the "role"')
def granted_permission(client, role, permission):
    """The permission is granted to the role."""
    from datadog_api_client.v2.model import relationship_to_permission
    from datadog_api_client.v2.model import relationship_to_permission_data
    from datadog_api_client.v2.api.roles_api import RolesApi

    api = RolesApi(client)
    body = relationship_to_permission.RelationshipToPermission(
        data=relationship_to_permission_data.RelationshipToPermissionData(
            id=permission.id, type=permission.type,
        )
    )
    return api.add_permission_to_role(role.data.id, body=body)


@given('the "user" has the "role"')
def user_has_role(vcr_cassette, client, user, role):
    """The user has the role."""
    from datadog_api_client.v2.exceptions import ApiException
    from datadog_api_client.v2.model import relationship_to_user
    from datadog_api_client.v2.model import relationship_to_user_data
    from datadog_api_client.v2.api.roles_api import RolesApi

    api = RolesApi(client)
    body = relationship_to_user.RelationshipToUser(
        data=relationship_to_user_data.RelationshipToUserData(
            id=user.data.id, type=str(user.data.type),
        )
    )
    yield api.add_user_to_role(role.data.id, body=body)
    if vcr_cassette.record_mode != "none":
        number_of_interactions = len(vcr_cassette.data)
        try:
            api.remove_user_from_role(role.data.id, body=body)
        except ApiException as e:
            warnings.warn(str(e))
        vcr_cassette.data = vcr_cassette.data[:number_of_interactions]


scenarios("features")
