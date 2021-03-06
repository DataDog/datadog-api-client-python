# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_monitoring_rule_severity import SecurityMonitoringRuleSeverity

globals()["SecurityMonitoringRuleSeverity"] = SecurityMonitoringRuleSeverity
from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase


class TestSecurityMonitoringRuleCase(unittest.TestCase):
    """SecurityMonitoringRuleCase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringRuleCase(self):
        """Test SecurityMonitoringRuleCase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringRuleCase()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
