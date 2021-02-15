# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.image_widget_definition_type import ImageWidgetDefinitionType
from datadog_api_client.v1.model.widget_image_sizing import WidgetImageSizing
from datadog_api_client.v1.model.widget_margin import WidgetMargin

globals()["ImageWidgetDefinitionType"] = ImageWidgetDefinitionType
globals()["WidgetImageSizing"] = WidgetImageSizing
globals()["WidgetMargin"] = WidgetMargin
from datadog_api_client.v1.model.image_widget_definition import ImageWidgetDefinition


class TestImageWidgetDefinition(unittest.TestCase):
    """ImageWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImageWidgetDefinition(self):
        """Test ImageWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ImageWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
