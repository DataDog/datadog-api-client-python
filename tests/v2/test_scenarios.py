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
                email=str(unique()) + "@datadoghq.com",
            ),
        ),
    )
    response = api["api"].create_user(body=body)
    yield response
    try:
        api["api"].disable_user(response.data.id)
    except ApiException as e:
        warnings.warn(e)


scenarios("features")
