# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import free_text_widget_definition_type
except ImportError:
    free_text_widget_definition_type = sys.modules["datadog_api_client.v1.model.free_text_widget_definition_type"]
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules["datadog_api_client.v1.model.widget_text_align"]
from datadog_api_client.v1.model.free_text_widget_definition import FreeTextWidgetDefinition


class TestFreeTextWidgetDefinition(unittest.TestCase):
    """FreeTextWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFreeTextWidgetDefinition(self):
        """Test FreeTextWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FreeTextWidgetDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
