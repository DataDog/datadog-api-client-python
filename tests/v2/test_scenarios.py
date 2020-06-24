# coding=utf-8
"""Test scenarios."""

import warnings

import pytest
from pytest_bdd import given, scenarios

pytestmark = pytest.mark.vcr


@given("there is a valid user in the system")
def user(api, unique):
    """There is a valid user in the system."""
    from datadog_api_client.v2.exceptions import ApiException
    from datadog_api_client.v2.model import user_create_request
    from datadog_api_client.v2.model import user_create_data
    from datadog_api_client.v2.model import user_create_attributes
    from datadog_api_client.v2.model import users_type

    body = user_create_request.UserCreateRequest(
        data=user_create_data.UserCreateData(
            type=users_type.UsersType(value="users"),
            attributes=user_create_attributes.UserCreateAttributes(
                email=str(unique) + "@datadoghq.com",
            ),
        ),
    )
    response = api["api"].create_user(body=body)
    yield response
    try:
        api["api"].disable_user(response.data.id)
    except ApiException as e:
        warnings.warn(str(e))


@given("there is a valid role in the system")
def role(api, unique):
    """There is a valid role in the system."""
    from datadog_api_client.v2.exceptions import ApiException
    from datadog_api_client.v2.model import role_create_request
    from datadog_api_client.v2.model import role_create_data
    from datadog_api_client.v2.model import role_create_attributes
    from datadog_api_client.v2.model import roles_type

    body = role_create_request.RoleCreateRequest(
        data=role_create_data.RoleCreateData(
            type=roles_type.RolesType(value="roles"),
            attributes=role_create_attributes.RoleCreateAttributes(
                name=str(unique),
            ),
        ),
    )
    response = api["api"].create_role(body=body)
    yield response
    try:
        api["api"].delete_role(response.data.id)
    except ApiException as e:
        warnings.warn(str(e))


@given("there is a valid permission in the system")
def permission(api):
    """There is a valid permission in the system."""
    return api["api"].list_permissions().data[0]


@given("the permission is granted to the role")
def granted_permission(api, role, permission):
    """The permission is granted to the role."""
    from datadog_api_client.v2.model import relationship_to_permission
    from datadog_api_client.v2.model import relationship_to_permission_data

    body = relationship_to_permission.RelationshipToPermission(
        data=relationship_to_permission_data.RelationshipToPermissionData(
            id=permission.id,
            type=permission.type,
        )
    )
    return api["api"].add_permission_to_role(role.data.id, body=body)


scenarios("features")
