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
    from datadog_api_client.v1.model import logs_pipeline_processor_type
except ImportError:
    logs_pipeline_processor_type = sys.modules["datadog_api_client.v1.model.logs_pipeline_processor_type"]
try:
    from datadog_api_client.v1.model import logs_processor
except ImportError:
    logs_processor = sys.modules["datadog_api_client.v1.model.logs_processor"]
from datadog_api_client.v1.model.logs_pipeline_processor import LogsPipelineProcessor


class TestLogsPipelineProcessor(unittest.TestCase):
    """LogsPipelineProcessor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsPipelineProcessor(self):
        """Test LogsPipelineProcessor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsPipelineProcessor()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
