# coding=utf-8
"""Test scenarios."""

import os
from pathlib import Path

import pytest
from pytest_bdd import scenarios


pytestmark = [pytest.mark.vcr(ignore_localhost=True)]

features = "features"
if "DD_TEST_RUNNER_DATA" in os.environ:
    features = str(Path(os.environ["DD_TEST_RUNNER_DATA"]) / "features" / "v2")

scenarios(features)
