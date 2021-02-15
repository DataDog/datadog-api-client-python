# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.monitor_summary_widget_definition_type import MonitorSummaryWidgetDefinitionType
from datadog_api_client.v1.model.widget_color_preference import WidgetColorPreference
from datadog_api_client.v1.model.widget_monitor_summary_display_format import WidgetMonitorSummaryDisplayFormat
from datadog_api_client.v1.model.widget_monitor_summary_sort import WidgetMonitorSummarySort
from datadog_api_client.v1.model.widget_summary_type import WidgetSummaryType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

globals()["MonitorSummaryWidgetDefinitionType"] = MonitorSummaryWidgetDefinitionType
globals()["WidgetColorPreference"] = WidgetColorPreference
globals()["WidgetMonitorSummaryDisplayFormat"] = WidgetMonitorSummaryDisplayFormat
globals()["WidgetMonitorSummarySort"] = WidgetMonitorSummarySort
globals()["WidgetSummaryType"] = WidgetSummaryType
globals()["WidgetTextAlign"] = WidgetTextAlign
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


if __name__ == "__main__":
    unittest.main()
