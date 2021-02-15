# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_processor import LogsProcessor

globals()["LogsFilter"] = LogsFilter
globals()["LogsProcessor"] = LogsProcessor
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
