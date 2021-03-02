# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType
from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus

globals()["SyntheticsAPITestConfig"] = SyntheticsAPITestConfig
globals()["SyntheticsAPITestType"] = SyntheticsAPITestType
globals()["SyntheticsTestDetailsSubType"] = SyntheticsTestDetailsSubType
globals()["SyntheticsTestOptions"] = SyntheticsTestOptions
globals()["SyntheticsTestPauseStatus"] = SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest


class TestSyntheticsAPITest(unittest.TestCase):
    """SyntheticsAPITest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAPITest(self):
        """Test SyntheticsAPITest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAPITest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
