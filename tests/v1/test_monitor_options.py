# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.monitor_device_id import MonitorDeviceID
from datadog_api_client.v1.model.monitor_options_aggregation import MonitorOptionsAggregation
from datadog_api_client.v1.model.monitor_threshold_window_options import MonitorThresholdWindowOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds

globals()["MonitorDeviceID"] = MonitorDeviceID
globals()["MonitorOptionsAggregation"] = MonitorOptionsAggregation
globals()["MonitorThresholdWindowOptions"] = MonitorThresholdWindowOptions
globals()["MonitorThresholds"] = MonitorThresholds
from datadog_api_client.v1.model.monitor_options import MonitorOptions


class TestMonitorOptions(unittest.TestCase):
    """MonitorOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitorOptions(self):
        """Test MonitorOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitorOptions()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
