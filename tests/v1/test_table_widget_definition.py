# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType
from datadog_api_client.v1.model.table_widget_has_search_bar import TableWidgetHasSearchBar
from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["TableWidgetDefinitionType"] = TableWidgetDefinitionType
globals()["TableWidgetHasSearchBar"] = TableWidgetHasSearchBar
globals()["TableWidgetRequest"] = TableWidgetRequest
globals()["WidgetCustomLink"] = WidgetCustomLink
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.table_widget_definition import TableWidgetDefinition


class TestTableWidgetDefinition(unittest.TestCase):
    """TableWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTableWidgetDefinition(self):
        """Test TableWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TableWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
