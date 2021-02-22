# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_forget_after import (
    SecurityMonitoringRuleNewValueOptionsForgetAfter,
)
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options_learning_duration import (
    SecurityMonitoringRuleNewValueOptionsLearningDuration,
)

globals()["SecurityMonitoringRuleNewValueOptionsForgetAfter"] = SecurityMonitoringRuleNewValueOptionsForgetAfter
globals()[
    "SecurityMonitoringRuleNewValueOptionsLearningDuration"
] = SecurityMonitoringRuleNewValueOptionsLearningDuration
from datadog_api_client.v2.model.security_monitoring_rule_new_value_options import SecurityMonitoringRuleNewValueOptions


class TestSecurityMonitoringRuleNewValueOptions(unittest.TestCase):
    """SecurityMonitoringRuleNewValueOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringRuleNewValueOptions(self):
        """Test SecurityMonitoringRuleNewValueOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringRuleNewValueOptions()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
