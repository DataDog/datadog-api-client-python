# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import logs_filter
except ImportError:
    logs_filter = sys.modules["datadog_api_client.v1.model.logs_filter"]
try:
    from datadog_api_client.v1.model import logs_processor
except ImportError:
    logs_processor = sys.modules["datadog_api_client.v1.model.logs_processor"]
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline


class TestLogsPipeline(unittest.TestCase):
    """LogsPipeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsPipeline(self):
        """Test LogsPipeline"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsPipeline()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
