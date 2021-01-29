# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import log
except ImportError:
    log = sys.modules["datadog_api_client.v2.model.log"]
try:
    from datadog_api_client.v2.model import logs_list_response_links
except ImportError:
    logs_list_response_links = sys.modules["datadog_api_client.v2.model.logs_list_response_links"]
from datadog_api_client.v2.model.logs_list_response import LogsListResponse


class TestLogsListResponse(unittest.TestCase):
    """LogsListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsListResponse(self):
        """Test LogsListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
