# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_arithmetic_processor import LogsArithmeticProcessor
from datadog_api_client.v1.model.logs_attribute_remapper import LogsAttributeRemapper
from datadog_api_client.v1.model.logs_category_processor import LogsCategoryProcessor
from datadog_api_client.v1.model.logs_category_processor_category import LogsCategoryProcessorCategory
from datadog_api_client.v1.model.logs_date_remapper import LogsDateRemapper
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_geo_ip_parser import LogsGeoIPParser
from datadog_api_client.v1.model.logs_grok_parser import LogsGrokParser
from datadog_api_client.v1.model.logs_grok_parser_rules import LogsGrokParserRules
from datadog_api_client.v1.model.logs_lookup_processor import LogsLookupProcessor
from datadog_api_client.v1.model.logs_message_remapper import LogsMessageRemapper
from datadog_api_client.v1.model.logs_pipeline_processor import LogsPipelineProcessor
from datadog_api_client.v1.model.logs_service_remapper import LogsServiceRemapper
from datadog_api_client.v1.model.logs_status_remapper import LogsStatusRemapper
from datadog_api_client.v1.model.logs_string_builder_processor import LogsStringBuilderProcessor
from datadog_api_client.v1.model.logs_trace_remapper import LogsTraceRemapper
from datadog_api_client.v1.model.logs_trace_remapper_type import LogsTraceRemapperType
from datadog_api_client.v1.model.logs_url_parser import LogsURLParser
from datadog_api_client.v1.model.logs_user_agent_parser import LogsUserAgentParser
from datadog_api_client.v1.model.target_format_type import TargetFormatType

globals()["LogsArithmeticProcessor"] = LogsArithmeticProcessor
globals()["LogsAttributeRemapper"] = LogsAttributeRemapper
globals()["LogsCategoryProcessor"] = LogsCategoryProcessor
globals()["LogsCategoryProcessorCategory"] = LogsCategoryProcessorCategory
globals()["LogsDateRemapper"] = LogsDateRemapper
globals()["LogsFilter"] = LogsFilter
globals()["LogsGeoIPParser"] = LogsGeoIPParser
globals()["LogsGrokParser"] = LogsGrokParser
globals()["LogsGrokParserRules"] = LogsGrokParserRules
globals()["LogsLookupProcessor"] = LogsLookupProcessor
globals()["LogsMessageRemapper"] = LogsMessageRemapper
globals()["LogsPipelineProcessor"] = LogsPipelineProcessor
globals()["LogsServiceRemapper"] = LogsServiceRemapper
globals()["LogsStatusRemapper"] = LogsStatusRemapper
globals()["LogsStringBuilderProcessor"] = LogsStringBuilderProcessor
globals()["LogsTraceRemapper"] = LogsTraceRemapper
globals()["LogsTraceRemapperType"] = LogsTraceRemapperType
globals()["LogsURLParser"] = LogsURLParser
globals()["LogsUserAgentParser"] = LogsUserAgentParser
globals()["TargetFormatType"] = TargetFormatType
from datadog_api_client.v1.model.logs_processor import LogsProcessor


class TestLogsProcessor(unittest.TestCase):
    """LogsProcessor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsProcessor(self):
        """Test LogsProcessor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsProcessor()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
