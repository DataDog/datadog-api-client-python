# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.check_status_widget_definition_type import CheckStatusWidgetDefinitionType
from datadog_api_client.v1.model.widget_grouping import WidgetGrouping
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
from datadog_api_client.v1.model.widget_time import WidgetTime

globals()["CheckStatusWidgetDefinitionType"] = CheckStatusWidgetDefinitionType
globals()["WidgetGrouping"] = WidgetGrouping
globals()["WidgetTextAlign"] = WidgetTextAlign
globals()["WidgetTime"] = WidgetTime
from datadog_api_client.v1.model.check_status_widget_definition import CheckStatusWidgetDefinition


class TestCheckStatusWidgetDefinition(unittest.TestCase):
    """CheckStatusWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCheckStatusWidgetDefinition(self):
        """Test CheckStatusWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CheckStatusWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
