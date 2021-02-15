# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_trigger_ci_test_location import SyntheticsTriggerCITestLocation
from datadog_api_client.v1.model.synthetics_trigger_ci_test_run_result import SyntheticsTriggerCITestRunResult

globals()["SyntheticsTriggerCITestLocation"] = SyntheticsTriggerCITestLocation
globals()["SyntheticsTriggerCITestRunResult"] = SyntheticsTriggerCITestRunResult
from datadog_api_client.v1.model.synthetics_trigger_ci_tests_response import SyntheticsTriggerCITestsResponse


class TestSyntheticsTriggerCITestsResponse(unittest.TestCase):
    """SyntheticsTriggerCITestsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsTriggerCITestsResponse(self):
        """Test SyntheticsTriggerCITestsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsTriggerCITestsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
