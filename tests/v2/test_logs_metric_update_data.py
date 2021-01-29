# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_metric_type import LogsMetricType
from datadog_api_client.v2.model.logs_metric_update_attributes import LogsMetricUpdateAttributes

globals()["LogsMetricType"] = LogsMetricType
globals()["LogsMetricUpdateAttributes"] = LogsMetricUpdateAttributes
from datadog_api_client.v2.model.logs_metric_update_data import LogsMetricUpdateData


class TestLogsMetricUpdateData(unittest.TestCase):
    """LogsMetricUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMetricUpdateData(self):
        """Test LogsMetricUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMetricUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
