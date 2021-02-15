# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_aggregate_bucket_value_timeseries_point import (
    LogsAggregateBucketValueTimeseriesPoint,
)

globals()["LogsAggregateBucketValueTimeseriesPoint"] = LogsAggregateBucketValueTimeseriesPoint
from datadog_api_client.v2.model.logs_aggregate_bucket_value_timeseries import LogsAggregateBucketValueTimeseries


class TestLogsAggregateBucketValueTimeseries(unittest.TestCase):
    """LogsAggregateBucketValueTimeseries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAggregateBucketValueTimeseries(self):
        """Test LogsAggregateBucketValueTimeseries"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAggregateBucketValueTimeseries()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
