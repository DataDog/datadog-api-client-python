# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_metric_category import UsageMetricCategory

globals()["UsageMetricCategory"] = UsageMetricCategory
from datadog_api_client.v1.model.usage_top_avg_metrics_hour import UsageTopAvgMetricsHour


class TestUsageTopAvgMetricsHour(unittest.TestCase):
    """UsageTopAvgMetricsHour unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageTopAvgMetricsHour(self):
        """Test UsageTopAvgMetricsHour"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageTopAvgMetricsHour()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
