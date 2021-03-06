# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.monitor_overall_states import MonitorOverallStates

globals()["MonitorOverallStates"] = MonitorOverallStates
from datadog_api_client.v1.model.monitor_state_group import MonitorStateGroup


class TestMonitorStateGroup(unittest.TestCase):
    """MonitorStateGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitorStateGroup(self):
        """Test MonitorStateGroup"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitorStateGroup()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
