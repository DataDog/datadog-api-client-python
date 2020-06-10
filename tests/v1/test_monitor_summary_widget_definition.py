# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import monitor_summary_widget_definition_type
except ImportError:
    monitor_summary_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.monitor_summary_widget_definition_type']
try:
    from datadog_api_client.v1.model import widget_color_preference
except ImportError:
    widget_color_preference = sys.modules[
        'datadog_api_client.v1.model.widget_color_preference']
try:
    from datadog_api_client.v1.model import widget_monitor_summary_display_format
except ImportError:
    widget_monitor_summary_display_format = sys.modules[
        'datadog_api_client.v1.model.widget_monitor_summary_display_format']
try:
    from datadog_api_client.v1.model import widget_monitor_summary_sort
except ImportError:
    widget_monitor_summary_sort = sys.modules[
        'datadog_api_client.v1.model.widget_monitor_summary_sort']
try:
    from datadog_api_client.v1.model import widget_summary_type
except ImportError:
    widget_summary_type = sys.modules[
        'datadog_api_client.v1.model.widget_summary_type']
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules[
        'datadog_api_client.v1.model.widget_text_align']
from datadog_api_client.v1.model.monitor_summary_widget_definition import MonitorSummaryWidgetDefinition


class TestMonitorSummaryWidgetDefinition(unittest.TestCase):
    """MonitorSummaryWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitorSummaryWidgetDefinition(self):
        """Test MonitorSummaryWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitorSummaryWidgetDefinition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
