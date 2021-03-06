# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_test_config import SyntheticsTestConfig

globals()["SyntheticsTestConfig"] = SyntheticsTestConfig
from datadog_api_client.v1.model.synthetics_api_test_result_full_check import SyntheticsAPITestResultFullCheck


class TestSyntheticsAPITestResultFullCheck(unittest.TestCase):
    """SyntheticsAPITestResultFullCheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAPITestResultFullCheck(self):
        """Test SyntheticsAPITestResultFullCheck"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAPITestResultFullCheck()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
