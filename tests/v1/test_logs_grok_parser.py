# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import logs_grok_parser_rules
except ImportError:
    logs_grok_parser_rules = sys.modules["datadog_api_client.v1.model.logs_grok_parser_rules"]
try:
    from datadog_api_client.v1.model import logs_grok_parser_type
except ImportError:
    logs_grok_parser_type = sys.modules["datadog_api_client.v1.model.logs_grok_parser_type"]
from datadog_api_client.v1.model.logs_grok_parser import LogsGrokParser


class TestLogsGrokParser(unittest.TestCase):
    """LogsGrokParser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsGrokParser(self):
        """Test LogsGrokParser"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsGrokParser()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
