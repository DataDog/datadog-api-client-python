# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_metric_response_compute_aggregation_type import (
    LogsMetricResponseComputeAggregationType,
)

globals()["LogsMetricResponseComputeAggregationType"] = LogsMetricResponseComputeAggregationType
from datadog_api_client.v2.model.logs_metric_response_compute import LogsMetricResponseCompute


class TestLogsMetricResponseCompute(unittest.TestCase):
    """LogsMetricResponseCompute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMetricResponseCompute(self):
        """Test LogsMetricResponseCompute"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMetricResponseCompute()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
