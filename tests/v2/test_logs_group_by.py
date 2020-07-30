# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import logs_aggregate_sort
except ImportError:
    logs_aggregate_sort = sys.modules[
        'datadog_api_client.v2.model.logs_aggregate_sort']
try:
    from datadog_api_client.v2.model import logs_group_by_histogram
except ImportError:
    logs_group_by_histogram = sys.modules[
        'datadog_api_client.v2.model.logs_group_by_histogram']
try:
    from datadog_api_client.v2.model import logs_group_by_missing
except ImportError:
    logs_group_by_missing = sys.modules[
        'datadog_api_client.v2.model.logs_group_by_missing']
try:
    from datadog_api_client.v2.model import logs_group_by_total
except ImportError:
    logs_group_by_total = sys.modules[
        'datadog_api_client.v2.model.logs_group_by_total']
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


if __name__ == '__main__':
    unittest.main()
