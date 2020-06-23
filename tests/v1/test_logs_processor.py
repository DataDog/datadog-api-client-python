# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import logs_arithmetic_processor
except ImportError:
    logs_arithmetic_processor = sys.modules[
        'datadog_api_client.v1.model.logs_arithmetic_processor']
try:
    from datadog_api_client.v1.model import logs_attribute_remapper
except ImportError:
    logs_attribute_remapper = sys.modules[
        'datadog_api_client.v1.model.logs_attribute_remapper']
try:
    from datadog_api_client.v1.model import logs_category_processor
except ImportError:
    logs_category_processor = sys.modules[
        'datadog_api_client.v1.model.logs_category_processor']
try:
    from datadog_api_client.v1.model import logs_category_processor_categories
except ImportError:
    logs_category_processor_categories = sys.modules[
        'datadog_api_client.v1.model.logs_category_processor_categories']
try:
    from datadog_api_client.v1.model import logs_date_remapper
except ImportError:
    logs_date_remapper = sys.modules[
        'datadog_api_client.v1.model.logs_date_remapper']
try:
    from datadog_api_client.v1.model import logs_filter
except ImportError:
    logs_filter = sys.modules[
        'datadog_api_client.v1.model.logs_filter']
try:
    from datadog_api_client.v1.model import logs_geo_ip_parser
except ImportError:
    logs_geo_ip_parser = sys.modules[
        'datadog_api_client.v1.model.logs_geo_ip_parser']
try:
    from datadog_api_client.v1.model import logs_grok_parser
except ImportError:
    logs_grok_parser = sys.modules[
        'datadog_api_client.v1.model.logs_grok_parser']
try:
    from datadog_api_client.v1.model import logs_grok_parser_rules
except ImportError:
    logs_grok_parser_rules = sys.modules[
        'datadog_api_client.v1.model.logs_grok_parser_rules']
try:
    from datadog_api_client.v1.model import logs_lookup_processor
except ImportError:
    logs_lookup_processor = sys.modules[
        'datadog_api_client.v1.model.logs_lookup_processor']
try:
    from datadog_api_client.v1.model import logs_message_remapper
except ImportError:
    logs_message_remapper = sys.modules[
        'datadog_api_client.v1.model.logs_message_remapper']
try:
    from datadog_api_client.v1.model import logs_pipeline_processor
except ImportError:
    logs_pipeline_processor = sys.modules[
        'datadog_api_client.v1.model.logs_pipeline_processor']
try:
    from datadog_api_client.v1.model import logs_service_remapper
except ImportError:
    logs_service_remapper = sys.modules[
        'datadog_api_client.v1.model.logs_service_remapper']
try:
    from datadog_api_client.v1.model import logs_status_remapper
except ImportError:
    logs_status_remapper = sys.modules[
        'datadog_api_client.v1.model.logs_status_remapper']
try:
    from datadog_api_client.v1.model import logs_string_builder_processor
except ImportError:
    logs_string_builder_processor = sys.modules[
        'datadog_api_client.v1.model.logs_string_builder_processor']
try:
    from datadog_api_client.v1.model import logs_trace_remapper
except ImportError:
    logs_trace_remapper = sys.modules[
        'datadog_api_client.v1.model.logs_trace_remapper']
try:
    from datadog_api_client.v1.model import logs_trace_remapper_type
except ImportError:
    logs_trace_remapper_type = sys.modules[
        'datadog_api_client.v1.model.logs_trace_remapper_type']
try:
    from datadog_api_client.v1.model import logs_url_parser
except ImportError:
    logs_url_parser = sys.modules[
        'datadog_api_client.v1.model.logs_url_parser']
try:
    from datadog_api_client.v1.model import logs_user_agent_parser
except ImportError:
    logs_user_agent_parser = sys.modules[
        'datadog_api_client.v1.model.logs_user_agent_parser']
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


if __name__ == '__main__':
    unittest.main()
