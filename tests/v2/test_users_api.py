# coding=utf-8
"""Test scenarios."""

import pytest
from pytest_bdd import given


@given("there is a valid user in the system")
def user(api, unique):
    """There is a valid user in the system."""
    from datadog_api_client.v2.model import user_create_payload
    from datadog_api_client.v2.model import user_create_data
    from datadog_api_client.v2.model import user_create_attributes
    from datadog_api_client.v2.model import users_type

    body = user_create_payload.UserCreatePayload(
        data=user_create_data.UserCreateData(
            type=users_type.UsersType(value="users"),
            attributes=user_create_attributes.UserCreateAttributes(
                email=str(unique()) + "@datadoghq.com",
            ),
        ),
    )
    response = api["api"].create_user(body=body)
    yield response
    api["api"].disable_user(response.data.id)


@given("parameter user_id from user.data.id")
def user_id(request, api_request, user):
    """Set request user_id."""
    api_request["kwargs"]["user_id"] = user.data.id
    return user_id
