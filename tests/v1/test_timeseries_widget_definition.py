# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_event import WidgetEvent
from datadog_api_client.v1.model.widget_marker import WidgetMarker
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["TimeseriesWidgetDefinitionType"] = TimeseriesWidgetDefinitionType
globals()["TimeseriesWidgetRequest"] = TimeseriesWidgetRequest
globals()["WidgetAxis"] = WidgetAxis
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetEvent"] = WidgetEvent
globals()["WidgetMarker"] = WidgetMarker
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition


class TestTimeseriesWidgetDefinition(unittest.TestCase):
    """TimeseriesWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeseriesWidgetDefinition(self):
        """Test TimeseriesWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeseriesWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
