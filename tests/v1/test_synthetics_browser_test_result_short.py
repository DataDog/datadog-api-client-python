# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_browser_test_result_short_result import (
    SyntheticsBrowserTestResultShortResult,
)
from datadog_api_client.v1.model.synthetics_test_monitor_status import SyntheticsTestMonitorStatus

globals()["SyntheticsBrowserTestResultShortResult"] = SyntheticsBrowserTestResultShortResult
globals()["SyntheticsTestMonitorStatus"] = SyntheticsTestMonitorStatus
from datadog_api_client.v1.model.synthetics_browser_test_result_short import SyntheticsBrowserTestResultShort


class TestSyntheticsBrowserTestResultShort(unittest.TestCase):
    """SyntheticsBrowserTestResultShort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsBrowserTestResultShort(self):
        """Test SyntheticsBrowserTestResultShort"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsBrowserTestResultShort()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
