# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import security_monitoring_rule_case
except ImportError:
    security_monitoring_rule_case = sys.modules["datadog_api_client.v2.model.security_monitoring_rule_case"]
try:
    from datadog_api_client.v2.model import security_monitoring_rule_options
except ImportError:
    security_monitoring_rule_options = sys.modules["datadog_api_client.v2.model.security_monitoring_rule_options"]
try:
    from datadog_api_client.v2.model import security_monitoring_rule_query
except ImportError:
    security_monitoring_rule_query = sys.modules["datadog_api_client.v2.model.security_monitoring_rule_query"]
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
