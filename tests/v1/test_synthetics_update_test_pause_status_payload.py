# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus

globals()["SyntheticsTestPauseStatus"] = SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_update_test_pause_status_payload import (
    SyntheticsUpdateTestPauseStatusPayload,
)


class TestSyntheticsUpdateTestPauseStatusPayload(unittest.TestCase):
    """SyntheticsUpdateTestPauseStatusPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsUpdateTestPauseStatusPayload(self):
        """Test SyntheticsUpdateTestPauseStatusPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsUpdateTestPauseStatusPayload()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
