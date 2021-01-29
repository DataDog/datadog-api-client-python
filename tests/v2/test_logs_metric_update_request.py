# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_metric_update_data import LogsMetricUpdateData

globals()["LogsMetricUpdateData"] = LogsMetricUpdateData
from datadog_api_client.v2.model.logs_metric_update_request import LogsMetricUpdateRequest


class TestLogsMetricUpdateRequest(unittest.TestCase):
    """LogsMetricUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMetricUpdateRequest(self):
        """Test LogsMetricUpdateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMetricUpdateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
