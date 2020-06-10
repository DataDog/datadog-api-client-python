# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import usage_top_avg_metrics_hour
except ImportError:
    usage_top_avg_metrics_hour = sys.modules[
        'datadog_api_client.v1.model.usage_top_avg_metrics_hour']
from datadog_api_client.v1.model.usage_top_avg_metrics_response import UsageTopAvgMetricsResponse


class TestUsageTopAvgMetricsResponse(unittest.TestCase):
    """UsageTopAvgMetricsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageTopAvgMetricsResponse(self):
        """Test UsageTopAvgMetricsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageTopAvgMetricsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
