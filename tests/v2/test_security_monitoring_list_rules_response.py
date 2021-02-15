# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes
from datadog_api_client.v2.model.security_monitoring_rule_response import SecurityMonitoringRuleResponse

globals()["ResponseMetaAttributes"] = ResponseMetaAttributes
globals()["SecurityMonitoringRuleResponse"] = SecurityMonitoringRuleResponse
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
