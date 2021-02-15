# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_basic_auth import SyntheticsBasicAuth
from datadog_api_client.v1.model.synthetics_ci_test_metadata import SyntheticsCITestMetadata
from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
from datadog_api_client.v1.model.synthetics_test_headers import SyntheticsTestHeaders
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry

globals()["SyntheticsBasicAuth"] = SyntheticsBasicAuth
globals()["SyntheticsCITestMetadata"] = SyntheticsCITestMetadata
globals()["SyntheticsDeviceID"] = SyntheticsDeviceID
globals()["SyntheticsTestHeaders"] = SyntheticsTestHeaders
globals()["SyntheticsTestOptionsRetry"] = SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_ci_test import SyntheticsCITest


class TestSyntheticsCITest(unittest.TestCase):
    """SyntheticsCITest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsCITest(self):
        """Test SyntheticsCITest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsCITest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
