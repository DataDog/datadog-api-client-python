# coding=utf-8
"""Define basic fixtures."""

import pytest

from datadog_api_client.v1 import ApiClient, Configuration


@pytest.fixture
def configuration():
    yield Configuration()


@pytest.fixture
def client(configuration):
    with ApiClient(configuration) as api_client:
        yield api_client
