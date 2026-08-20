# coding=utf-8
"""Test scenarios."""

import os

import pytest
from pytest_bdd import scenarios


pytestmark = [] if "DD_TEST_SERVER_URL" in os.environ else [pytest.mark.vcr(ignore_localhost=True)]

scenarios("features")
