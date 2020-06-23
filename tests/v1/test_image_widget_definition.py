# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import image_widget_definition_type
except ImportError:
    image_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.image_widget_definition_type']
try:
    from datadog_api_client.v1.model import widget_image_sizing
except ImportError:
    widget_image_sizing = sys.modules[
        'datadog_api_client.v1.model.widget_image_sizing']
try:
    from datadog_api_client.v1.model import widget_margin
except ImportError:
    widget_margin = sys.modules[
        'datadog_api_client.v1.model.widget_margin']
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


if __name__ == '__main__':
    unittest.main()
