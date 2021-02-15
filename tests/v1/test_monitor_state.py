# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.monitor_state_group import MonitorStateGroup

globals()["MonitorStateGroup"] = MonitorStateGroup
from datadog_api_client.v1.model.monitor_state import MonitorState


class TestMonitorState(unittest.TestCase):
    """MonitorState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitorState(self):
        """Test MonitorState"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitorState()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
