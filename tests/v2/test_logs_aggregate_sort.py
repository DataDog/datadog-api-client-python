# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import logs_aggregate_sort_type
except ImportError:
    logs_aggregate_sort_type = sys.modules[
        'datadog_api_client.v2.model.logs_aggregate_sort_type']
try:
    from datadog_api_client.v2.model import logs_aggregation_function
except ImportError:
    logs_aggregation_function = sys.modules[
        'datadog_api_client.v2.model.logs_aggregation_function']
try:
    from datadog_api_client.v2.model import logs_sort_order
except ImportError:
    logs_sort_order = sys.modules[
        'datadog_api_client.v2.model.logs_sort_order']
from datadog_api_client.v2.model.logs_aggregate_sort import LogsAggregateSort


class TestLogsAggregateSort(unittest.TestCase):
    """LogsAggregateSort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAggregateSort(self):
        """Test LogsAggregateSort"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAggregateSort()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
