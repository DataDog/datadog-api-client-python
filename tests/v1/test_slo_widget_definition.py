# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import slo_widget_definition_type
except ImportError:
    slo_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.slo_widget_definition_type']
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules[
        'datadog_api_client.v1.model.widget_text_align']
try:
    from datadog_api_client.v1.model import widget_time_windows
except ImportError:
    widget_time_windows = sys.modules[
        'datadog_api_client.v1.model.widget_time_windows']
try:
    from datadog_api_client.v1.model import widget_view_mode
except ImportError:
    widget_view_mode = sys.modules[
        'datadog_api_client.v1.model.widget_view_mode']
from datadog_api_client.v1.model.slo_widget_definition import SLOWidgetDefinition


class TestSLOWidgetDefinition(unittest.TestCase):
    """SLOWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOWidgetDefinition(self):
        """Test SLOWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOWidgetDefinition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
