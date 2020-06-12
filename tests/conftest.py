# coding=utf-8
"""Define basic fixtures."""

import os

from pytest_bdd import given

@given('a valid API key')
def a_valid_api_key(configuration):
    """a valid API key."""
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY")


@given('a valid Application key')
def a_valid_application_key(configuration):
    """a valid Application key."""
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY")
