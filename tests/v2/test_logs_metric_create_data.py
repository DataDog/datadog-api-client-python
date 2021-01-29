# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_metric_create_attributes import LogsMetricCreateAttributes
from datadog_api_client.v2.model.logs_metric_type import LogsMetricType

globals()["LogsMetricCreateAttributes"] = LogsMetricCreateAttributes
globals()["LogsMetricType"] = LogsMetricType
from datadog_api_client.v2.model.logs_metric_create_data import LogsMetricCreateData


class TestLogsMetricCreateData(unittest.TestCase):
    """LogsMetricCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMetricCreateData(self):
        """Test LogsMetricCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMetricCreateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
