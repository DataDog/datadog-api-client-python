# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.creator import Creator
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_overall_states import MonitorOverallStates
from datadog_api_client.v1.model.monitor_state import MonitorState
from datadog_api_client.v1.model.monitor_type import MonitorType

globals()["Creator"] = Creator
globals()["MonitorOptions"] = MonitorOptions
globals()["MonitorOverallStates"] = MonitorOverallStates
globals()["MonitorState"] = MonitorState
globals()["MonitorType"] = MonitorType
from datadog_api_client.v1.model.monitor import Monitor


class TestMonitor(unittest.TestCase):
    """Monitor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitor(self):
        """Test Monitor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Monitor()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
