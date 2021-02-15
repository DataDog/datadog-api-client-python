# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.event_timeline_widget_definition_type import EventTimelineWidgetDefinitionType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["EventTimelineWidgetDefinitionType"] = EventTimelineWidgetDefinitionType
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.event_timeline_widget_definition import EventTimelineWidgetDefinition


class TestEventTimelineWidgetDefinition(unittest.TestCase):
    """EventTimelineWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventTimelineWidgetDefinition(self):
        """Test EventTimelineWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventTimelineWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
