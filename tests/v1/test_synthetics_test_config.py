# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import synthetics_assertion
except ImportError:
    synthetics_assertion = sys.modules["datadog_api_client.v1.model.synthetics_assertion"]
try:
    from datadog_api_client.v1.model import synthetics_browser_variable
except ImportError:
    synthetics_browser_variable = sys.modules["datadog_api_client.v1.model.synthetics_browser_variable"]
try:
    from datadog_api_client.v1.model import synthetics_test_request
except ImportError:
    synthetics_test_request = sys.modules["datadog_api_client.v1.model.synthetics_test_request"]
from datadog_api_client.v1.model.synthetics_test_config import SyntheticsTestConfig


class TestSyntheticsTestConfig(unittest.TestCase):
    """SyntheticsTestConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsTestConfig(self):
        """Test SyntheticsTestConfig"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsTestConfig()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
