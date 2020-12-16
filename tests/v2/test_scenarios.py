# coding=utf-8
"""Test scenarios."""

import pytest
from pytest_bdd import scenarios


pytestmark = [
    pytest.mark.vcr(ignore_localhost=True),
    pytest.mark.usefixtures("context", "client", "freezer"),
]

scenarios("features")
