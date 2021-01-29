# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import logs_aggregate_response_data
except ImportError:
    logs_aggregate_response_data = sys.modules["datadog_api_client.v2.model.logs_aggregate_response_data"]
try:
    from datadog_api_client.v2.model import logs_response_metadata
except ImportError:
    logs_response_metadata = sys.modules["datadog_api_client.v2.model.logs_response_metadata"]
from datadog_api_client.v2.model.logs_aggregate_response import LogsAggregateResponse


class TestLogsAggregateResponse(unittest.TestCase):
    """LogsAggregateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAggregateResponse(self):
        """Test LogsAggregateResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAggregateResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
