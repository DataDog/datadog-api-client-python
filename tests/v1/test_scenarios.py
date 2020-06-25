# coding=utf-8
"""Test scenarios."""

import pytest
from pytest_bdd import scenarios


pytestmark = [
    pytest.mark.vcr(
        match_on=("method", "scheme", "host", "port", "path", "query", "body")
    ),
    pytest.mark.usefixtures("ddspan"),
]

scenarios('features')
