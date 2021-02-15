# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline_processor_type import LogsPipelineProcessorType
from datadog_api_client.v1.model.logs_processor import LogsProcessor

globals()["LogsFilter"] = LogsFilter
globals()["LogsPipelineProcessorType"] = LogsPipelineProcessorType
globals()["LogsProcessor"] = LogsProcessor
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
