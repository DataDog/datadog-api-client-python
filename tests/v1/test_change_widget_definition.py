# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.change_widget_definition_type import ChangeWidgetDefinitionType
from datadog_api_client.v1.model.change_widget_request import ChangeWidgetRequest
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["ChangeWidgetDefinitionType"] = ChangeWidgetDefinitionType
globals()["ChangeWidgetRequest"] = ChangeWidgetRequest
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.change_widget_definition import ChangeWidgetDefinition


class TestChangeWidgetDefinition(unittest.TestCase):
    """ChangeWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangeWidgetDefinition(self):
        """Test ChangeWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChangeWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
