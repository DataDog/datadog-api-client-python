# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_metric_compute import LogsMetricCompute
from datadog_api_client.v2.model.logs_metric_filter import LogsMetricFilter
from datadog_api_client.v2.model.logs_metric_group_by import LogsMetricGroupBy

globals()["LogsMetricCompute"] = LogsMetricCompute
globals()["LogsMetricFilter"] = LogsMetricFilter
globals()["LogsMetricGroupBy"] = LogsMetricGroupBy
from datadog_api_client.v2.model.logs_metric_create_attributes import LogsMetricCreateAttributes


class TestLogsMetricCreateAttributes(unittest.TestCase):
    """LogsMetricCreateAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMetricCreateAttributes(self):
        """Test LogsMetricCreateAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMetricCreateAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
