# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.group_widget_definition_type import GroupWidgetDefinitionType
from datadog_api_client.v1.model.widget import Widget
from datadog_api_client.v1.model.widget_layout_type import WidgetLayoutType

globals()["GroupWidgetDefinitionType"] = GroupWidgetDefinitionType
globals()["Widget"] = Widget
globals()["WidgetLayoutType"] = WidgetLayoutType
from datadog_api_client.v1.model.group_widget_definition import GroupWidgetDefinition


class TestGroupWidgetDefinition(unittest.TestCase):
    """GroupWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroupWidgetDefinition(self):
        """Test GroupWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GroupWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
