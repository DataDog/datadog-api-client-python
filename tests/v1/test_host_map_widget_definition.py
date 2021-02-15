# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.host_map_widget_definition_requests import HostMapWidgetDefinitionRequests
from datadog_api_client.v1.model.host_map_widget_definition_style import HostMapWidgetDefinitionStyle
from datadog_api_client.v1.model.host_map_widget_definition_type import HostMapWidgetDefinitionType
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_node_type import WidgetNodeType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

globals()["HostMapWidgetDefinitionRequests"] = HostMapWidgetDefinitionRequests
globals()["HostMapWidgetDefinitionStyle"] = HostMapWidgetDefinitionStyle
globals()["HostMapWidgetDefinitionType"] = HostMapWidgetDefinitionType
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetNodeType"] = WidgetNodeType
globals()["WidgetTextAlign"] = WidgetTextAlign
from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition


class TestHostMapWidgetDefinition(unittest.TestCase):
    """HostMapWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHostMapWidgetDefinition(self):
        """Test HostMapWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HostMapWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
