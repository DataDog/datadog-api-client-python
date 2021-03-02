# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_browser_test_config import SyntheticsBrowserTestConfig
from datadog_api_client.v1.model.synthetics_browser_test_type import SyntheticsBrowserTestType
from datadog_api_client.v1.model.synthetics_step import SyntheticsStep
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus

globals()["SyntheticsBrowserTestConfig"] = SyntheticsBrowserTestConfig
globals()["SyntheticsBrowserTestType"] = SyntheticsBrowserTestType
globals()["SyntheticsStep"] = SyntheticsStep
globals()["SyntheticsTestOptions"] = SyntheticsTestOptions
globals()["SyntheticsTestPauseStatus"] = SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_browser_test import SyntheticsBrowserTest


class TestSyntheticsBrowserTest(unittest.TestCase):
    """SyntheticsBrowserTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsBrowserTest(self):
        """Test SyntheticsBrowserTest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsBrowserTest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
