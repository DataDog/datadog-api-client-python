# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.query_value_widget_definition_type import QueryValueWidgetDefinitionType
from datadog_api_client.v1.model.query_value_widget_request import QueryValueWidgetRequest
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["QueryValueWidgetDefinitionType"] = QueryValueWidgetDefinitionType
globals()["QueryValueWidgetRequest"] = QueryValueWidgetRequest
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition


class TestQueryValueWidgetDefinition(unittest.TestCase):
    """QueryValueWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQueryValueWidgetDefinition(self):
        """Test QueryValueWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QueryValueWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
