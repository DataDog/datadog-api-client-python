# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.scatter_plot_widget_definition_requests import ScatterPlotWidgetDefinitionRequests
from datadog_api_client.v1.model.scatter_plot_widget_definition_type import ScatterPlotWidgetDefinitionType
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["ScatterPlotWidgetDefinitionRequests"] = ScatterPlotWidgetDefinitionRequests
globals()["ScatterPlotWidgetDefinitionType"] = ScatterPlotWidgetDefinitionType
globals()["WidgetAxis"] = WidgetAxis
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.scatter_plot_widget_definition import ScatterPlotWidgetDefinition


class TestScatterPlotWidgetDefinition(unittest.TestCase):
    """ScatterPlotWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScatterPlotWidgetDefinition(self):
        """Test ScatterPlotWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScatterPlotWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
