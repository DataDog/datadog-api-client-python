# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_metric_response_compute import LogsMetricResponseCompute
from datadog_api_client.v2.model.logs_metric_response_filter import LogsMetricResponseFilter
from datadog_api_client.v2.model.logs_metric_response_group_by import LogsMetricResponseGroupBy
globals()['LogsMetricResponseCompute'] = LogsMetricResponseCompute
globals()['LogsMetricResponseFilter'] = LogsMetricResponseFilter
globals()['LogsMetricResponseGroupBy'] = LogsMetricResponseGroupBy
from datadog_api_client.v2.model.logs_metric_response_attributes import LogsMetricResponseAttributes


class TestLogsMetricResponseAttributes(unittest.TestCase):
    """LogsMetricResponseAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMetricResponseAttributes(self):
        """Test LogsMetricResponseAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMetricResponseAttributes()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
