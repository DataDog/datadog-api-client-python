# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_aggregate_sort import LogsAggregateSort
from datadog_api_client.v2.model.logs_group_by_histogram import LogsGroupByHistogram
from datadog_api_client.v2.model.logs_group_by_missing import LogsGroupByMissing
from datadog_api_client.v2.model.logs_group_by_total import LogsGroupByTotal

globals()["LogsAggregateSort"] = LogsAggregateSort
globals()["LogsGroupByHistogram"] = LogsGroupByHistogram
globals()["LogsGroupByMissing"] = LogsGroupByMissing
globals()["LogsGroupByTotal"] = LogsGroupByTotal
from datadog_api_client.v2.model.logs_group_by import LogsGroupBy


class TestLogsGroupBy(unittest.TestCase):
    """LogsGroupBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsGroupBy(self):
        """Test LogsGroupBy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsGroupBy()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
