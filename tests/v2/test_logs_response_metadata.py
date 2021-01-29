# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import logs_aggregate_response_status
except ImportError:
    logs_aggregate_response_status = sys.modules["datadog_api_client.v2.model.logs_aggregate_response_status"]
try:
    from datadog_api_client.v2.model import logs_response_metadata_page
except ImportError:
    logs_response_metadata_page = sys.modules["datadog_api_client.v2.model.logs_response_metadata_page"]
try:
    from datadog_api_client.v2.model import logs_warning
except ImportError:
    logs_warning = sys.modules["datadog_api_client.v2.model.logs_warning"]
from datadog_api_client.v2.model.logs_response_metadata import LogsResponseMetadata


class TestLogsResponseMetadata(unittest.TestCase):
    """LogsResponseMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsResponseMetadata(self):
        """Test LogsResponseMetadata"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsResponseMetadata()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
