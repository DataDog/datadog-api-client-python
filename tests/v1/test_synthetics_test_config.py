# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
from datadog_api_client.v1.model.synthetics_browser_variable import SyntheticsBrowserVariable
from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

globals()["SyntheticsAssertion"] = SyntheticsAssertion
globals()["SyntheticsBrowserVariable"] = SyntheticsBrowserVariable
globals()["SyntheticsConfigVariable"] = SyntheticsConfigVariable
globals()["SyntheticsTestRequest"] = SyntheticsTestRequest
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
