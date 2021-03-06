# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
from datadog_api_client.v2.model.security_monitoring_rule_query_create import SecurityMonitoringRuleQueryCreate

globals()["SecurityMonitoringFilter"] = SecurityMonitoringFilter
globals()["SecurityMonitoringRuleCaseCreate"] = SecurityMonitoringRuleCaseCreate
globals()["SecurityMonitoringRuleOptions"] = SecurityMonitoringRuleOptions
globals()["SecurityMonitoringRuleQueryCreate"] = SecurityMonitoringRuleQueryCreate
from datadog_api_client.v2.model.security_monitoring_rule_create_payload import SecurityMonitoringRuleCreatePayload


class TestSecurityMonitoringRuleCreatePayload(unittest.TestCase):
    """SecurityMonitoringRuleCreatePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringRuleCreatePayload(self):
        """Test SecurityMonitoringRuleCreatePayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringRuleCreatePayload()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
