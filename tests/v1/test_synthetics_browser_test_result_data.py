# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_device import SyntheticsDevice
from datadog_api_client.v1.model.synthetics_step_detail import SyntheticsStepDetail

globals()["SyntheticsDevice"] = SyntheticsDevice
globals()["SyntheticsStepDetail"] = SyntheticsStepDetail
from datadog_api_client.v1.model.synthetics_browser_test_result_data import SyntheticsBrowserTestResultData


class TestSyntheticsBrowserTestResultData(unittest.TestCase):
    """SyntheticsBrowserTestResultData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsBrowserTestResultData(self):
        """Test SyntheticsBrowserTestResultData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsBrowserTestResultData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
