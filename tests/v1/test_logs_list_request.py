# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import logs_list_request_time
except ImportError:
    logs_list_request_time = sys.modules[
        'datadog_api_client.v1.model.logs_list_request_time']
try:
    from datadog_api_client.v1.model import logs_sort
except ImportError:
    logs_sort = sys.modules[
        'datadog_api_client.v1.model.logs_sort']
from datadog_api_client.v1.model.logs_list_request import LogsListRequest


class TestLogsListRequest(unittest.TestCase):
    """LogsListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsListRequest(self):
        """Test LogsListRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsListRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
