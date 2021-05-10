# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_retention_sum_usage import LogsRetentionSumUsage

globals()["LogsRetentionSumUsage"] = LogsRetentionSumUsage
from datadog_api_client.v1.model.logs_by_retention_monthly_usage import LogsByRetentionMonthlyUsage


class TestLogsByRetentionMonthlyUsage(unittest.TestCase):
    """LogsByRetentionMonthlyUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsByRetentionMonthlyUsage(self):
        """Test LogsByRetentionMonthlyUsage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsByRetentionMonthlyUsage()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
