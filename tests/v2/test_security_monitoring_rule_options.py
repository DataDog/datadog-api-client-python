# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import security_monitoring_rule_evaluation_window
except ImportError:
    security_monitoring_rule_evaluation_window = sys.modules[
        "datadog_api_client.v2.model.security_monitoring_rule_evaluation_window"
    ]
try:
    from datadog_api_client.v2.model import security_monitoring_rule_keep_alive
except ImportError:
    security_monitoring_rule_keep_alive = sys.modules["datadog_api_client.v2.model.security_monitoring_rule_keep_alive"]
try:
    from datadog_api_client.v2.model import security_monitoring_rule_max_signal_duration
except ImportError:
    security_monitoring_rule_max_signal_duration = sys.modules[
        "datadog_api_client.v2.model.security_monitoring_rule_max_signal_duration"
    ]
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions


class TestSecurityMonitoringRuleOptions(unittest.TestCase):
    """SecurityMonitoringRuleOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringRuleOptions(self):
        """Test SecurityMonitoringRuleOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringRuleOptions()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
