# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_query import SecurityMonitoringRuleQuery

globals()["SecurityMonitoringFilter"] = SecurityMonitoringFilter
globals()["SecurityMonitoringRuleCase"] = SecurityMonitoringRuleCase
globals()["SecurityMonitoringRuleOptions"] = SecurityMonitoringRuleOptions
globals()["SecurityMonitoringRuleQuery"] = SecurityMonitoringRuleQuery
from datadog_api_client.v2.model.security_monitoring_rule_response import SecurityMonitoringRuleResponse


class TestSecurityMonitoringRuleResponse(unittest.TestCase):
    """SecurityMonitoringRuleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringRuleResponse(self):
        """Test SecurityMonitoringRuleResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringRuleResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
