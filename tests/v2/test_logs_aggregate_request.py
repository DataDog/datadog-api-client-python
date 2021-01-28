# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import logs_aggregate_request_page
except ImportError:
    logs_aggregate_request_page = sys.modules[
        'datadog_api_client.v2.model.logs_aggregate_request_page']
try:
    from datadog_api_client.v2.model import logs_compute
except ImportError:
    logs_compute = sys.modules[
        'datadog_api_client.v2.model.logs_compute']
try:
    from datadog_api_client.v2.model import logs_group_by
except ImportError:
    logs_group_by = sys.modules[
        'datadog_api_client.v2.model.logs_group_by']
try:
    from datadog_api_client.v2.model import logs_query_filter
except ImportError:
    logs_query_filter = sys.modules[
        'datadog_api_client.v2.model.logs_query_filter']
try:
    from datadog_api_client.v2.model import logs_query_options
except ImportError:
    logs_query_options = sys.modules[
        'datadog_api_client.v2.model.logs_query_options']
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


if __name__ == '__main__':
    unittest.main()
