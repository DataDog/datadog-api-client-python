# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import log_stream_widget_definition_type
except ImportError:
    log_stream_widget_definition_type = sys.modules["datadog_api_client.v1.model.log_stream_widget_definition_type"]
try:
    from datadog_api_client.v1.model import widget_field_sort
except ImportError:
    widget_field_sort = sys.modules["datadog_api_client.v1.model.widget_field_sort"]
try:
    from datadog_api_client.v1.model import widget_message_display
except ImportError:
    widget_message_display = sys.modules["datadog_api_client.v1.model.widget_message_display"]
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules["datadog_api_client.v1.model.widget_text_align"]
try:
    from datadog_api_client.v1.model import widget_time
except ImportError:
    widget_time = sys.modules["datadog_api_client.v1.model.widget_time"]
from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition


class TestLogStreamWidgetDefinition(unittest.TestCase):
    """LogStreamWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogStreamWidgetDefinition(self):
        """Test LogStreamWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogStreamWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
