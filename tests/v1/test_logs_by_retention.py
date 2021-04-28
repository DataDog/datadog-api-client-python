# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_by_retention_monthly_usage import LogsByRetentionMonthlyUsage
from datadog_api_client.v1.model.logs_by_retention_orgs import LogsByRetentionOrgs
from datadog_api_client.v1.model.logs_retention_agg_sum_usage import LogsRetentionAggSumUsage

globals()["LogsByRetentionMonthlyUsage"] = LogsByRetentionMonthlyUsage
globals()["LogsByRetentionOrgs"] = LogsByRetentionOrgs
globals()["LogsRetentionAggSumUsage"] = LogsRetentionAggSumUsage
from datadog_api_client.v1.model.logs_by_retention import LogsByRetention


class TestLogsByRetention(unittest.TestCase):
    """LogsByRetention unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsByRetention(self):
        """Test LogsByRetention"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsByRetention()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
