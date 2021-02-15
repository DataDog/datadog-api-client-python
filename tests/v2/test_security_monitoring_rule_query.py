# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
    SecurityMonitoringRuleQueryAggregation,
)

globals()["SecurityMonitoringRuleQueryAggregation"] = SecurityMonitoringRuleQueryAggregation
from datadog_api_client.v2.model.security_monitoring_rule_query import SecurityMonitoringRuleQuery


class TestSecurityMonitoringRuleQuery(unittest.TestCase):
    """SecurityMonitoringRuleQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringRuleQuery(self):
        """Test SecurityMonitoringRuleQuery"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringRuleQuery()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
