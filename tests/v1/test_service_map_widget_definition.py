# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.service_map_widget_definition_type import ServiceMapWidgetDefinitionType
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

globals()["ServiceMapWidgetDefinitionType"] = ServiceMapWidgetDefinitionType
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetTextAlign"] = WidgetTextAlign
from datadog_api_client.v1.model.service_map_widget_definition import ServiceMapWidgetDefinition


class TestServiceMapWidgetDefinition(unittest.TestCase):
    """ServiceMapWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceMapWidgetDefinition(self):
        """Test ServiceMapWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceMapWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
