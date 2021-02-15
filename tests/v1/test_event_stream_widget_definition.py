# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.event_stream_widget_definition_type import EventStreamWidgetDefinitionType
from datadog_api_client.v1.model.widget_event_size import WidgetEventSize
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["EventStreamWidgetDefinitionType"] = EventStreamWidgetDefinitionType
globals()["WidgetEventSize"] = WidgetEventSize
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.event_stream_widget_definition import EventStreamWidgetDefinition


class TestEventStreamWidgetDefinition(unittest.TestCase):
    """EventStreamWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventStreamWidgetDefinition(self):
        """Test EventStreamWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventStreamWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
