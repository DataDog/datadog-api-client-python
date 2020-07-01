# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import logs_list_response_meta_page
except ImportError:
    logs_list_response_meta_page = sys.modules[
        'datadog_api_client.v2.model.logs_list_response_meta_page']
from datadog_api_client.v2.model.logs_list_response_meta import LogsListResponseMeta


class TestLogsListResponseMeta(unittest.TestCase):
    """LogsListResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsListResponseMeta(self):
        """Test LogsListResponseMeta"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsListResponseMeta()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
