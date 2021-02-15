# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_aggregate_request_page import LogsAggregateRequestPage
from datadog_api_client.v2.model.logs_compute import LogsCompute
from datadog_api_client.v2.model.logs_group_by import LogsGroupBy
from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
from datadog_api_client.v2.model.logs_query_options import LogsQueryOptions

globals()["LogsAggregateRequestPage"] = LogsAggregateRequestPage
globals()["LogsCompute"] = LogsCompute
globals()["LogsGroupBy"] = LogsGroupBy
globals()["LogsQueryFilter"] = LogsQueryFilter
globals()["LogsQueryOptions"] = LogsQueryOptions
from datadog_api_client.v2.model.logs_aggregate_request import LogsAggregateRequest


class TestLogsAggregateRequest(unittest.TestCase):
    """LogsAggregateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAggregateRequest(self):
        """Test LogsAggregateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAggregateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
