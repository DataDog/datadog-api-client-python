# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.event_query_definition import EventQueryDefinition
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
from datadog_api_client.v1.model.widget_style import WidgetStyle

globals()["EventQueryDefinition"] = EventQueryDefinition
globals()["LogQueryDefinition"] = LogQueryDefinition
globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
globals()["WidgetStyle"] = WidgetStyle
from datadog_api_client.v1.model.heat_map_widget_request import HeatMapWidgetRequest


class TestHeatMapWidgetRequest(unittest.TestCase):
    """HeatMapWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHeatMapWidgetRequest(self):
        """Test HeatMapWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HeatMapWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
