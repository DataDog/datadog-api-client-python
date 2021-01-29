# coding=utf-8
"""Define basic fixtures."""

import pytest
from pytest_bdd import given


@pytest.fixture(scope="module")
def package_name():
    return "datadog_api_client.v2"
