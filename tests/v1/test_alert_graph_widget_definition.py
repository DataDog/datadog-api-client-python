# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.alert_graph_widget_definition_type import AlertGraphWidgetDefinitionType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime
from datadog_api_client.v1.model.widget_viz_type import WidgetVizType

globals()["AlertGraphWidgetDefinitionType"] = AlertGraphWidgetDefinitionType
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
globals()["WidgetVizType"] = WidgetVizType
from datadog_api_client.v1.model.alert_graph_widget_definition import AlertGraphWidgetDefinition


class TestAlertGraphWidgetDefinition(unittest.TestCase):
    """AlertGraphWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAlertGraphWidgetDefinition(self):
        """Test AlertGraphWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AlertGraphWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
