# coding=utf-8
"""Test scenarios."""

import pytest
from pytest_bdd import scenarios


pytestmark = [pytest.mark.vcr(ignore_localhost=True)]

scenarios("features")
