# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_metric_compute_aggregation_type import LogsMetricComputeAggregationType

globals()["LogsMetricComputeAggregationType"] = LogsMetricComputeAggregationType
from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute


class TestLogsMetricCompute(unittest.TestCase):
    """LogsMetricCompute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMetricCompute(self):
        """Test LogsMetricCompute"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMetricCompute()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
