# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.slo_widget_definition_type import SLOWidgetDefinitionType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time_windows import WidgetTimeWindows
from datadog_api_client.v1.model.widget_view_mode import WidgetViewMode

globals()["SLOWidgetDefinitionType"] = SLOWidgetDefinitionType
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTimeWindows"] = WidgetTimeWindows
globals()["WidgetViewMode"] = WidgetViewMode
from datadog_api_client.v1.model.slo_widget_definition import SLOWidgetDefinition


class TestSLOWidgetDefinition(unittest.TestCase):
    """SLOWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOWidgetDefinition(self):
        """Test SLOWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
