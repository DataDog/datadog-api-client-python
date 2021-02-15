# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.alert_value_widget_definition_type import AlertValueWidgetDefinitionType
from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

globals()["AlertValueWidgetDefinitionType"] = AlertValueWidgetDefinitionType
globals()["WidgetTextAlign"] = WidgetTextAlign
from datadog_api_client.v1.model.alert_value_widget_definition import AlertValueWidgetDefinition


class TestAlertValueWidgetDefinition(unittest.TestCase):
    """AlertValueWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAlertValueWidgetDefinition(self):
        """Test AlertValueWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AlertValueWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
