# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import log_query_definition_group_by
except ImportError:
    log_query_definition_group_by = sys.modules["datadog_api_client.v1.model.log_query_definition_group_by"]
try:
    from datadog_api_client.v1.model import log_query_definition_search
except ImportError:
    log_query_definition_search = sys.modules["datadog_api_client.v1.model.log_query_definition_search"]
try:
    from datadog_api_client.v1.model import logs_query_compute
except ImportError:
    logs_query_compute = sys.modules["datadog_api_client.v1.model.logs_query_compute"]
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition


class TestLogQueryDefinition(unittest.TestCase):
    """LogQueryDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogQueryDefinition(self):
        """Test LogQueryDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogQueryDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
