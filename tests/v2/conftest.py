# coding=utf-8
"""Define basic fixtures."""

import pytest


@pytest.fixture(scope="module")
def api_version():
    return "v2"
