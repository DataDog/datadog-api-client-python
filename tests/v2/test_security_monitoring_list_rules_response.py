# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import response_meta_attributes
except ImportError:
    response_meta_attributes = sys.modules["datadog_api_client.v2.model.response_meta_attributes"]
try:
    from datadog_api_client.v2.model import security_monitoring_rule_response
except ImportError:
    security_monitoring_rule_response = sys.modules["datadog_api_client.v2.model.security_monitoring_rule_response"]
from datadog_api_client.v2.model.security_monitoring_list_rules_response import SecurityMonitoringListRulesResponse


class TestSecurityMonitoringListRulesResponse(unittest.TestCase):
    """SecurityMonitoringListRulesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringListRulesResponse(self):
        """Test SecurityMonitoringListRulesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringListRulesResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
