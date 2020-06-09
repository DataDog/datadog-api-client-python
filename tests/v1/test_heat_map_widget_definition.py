# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import heat_map_widget_definition_type
except ImportError:
    heat_map_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.heat_map_widget_definition_type']
try:
    from datadog_api_client.v1.model import heat_map_widget_request
except ImportError:
    heat_map_widget_request = sys.modules[
        'datadog_api_client.v1.model.heat_map_widget_request']
try:
    from datadog_api_client.v1.model import widget_axis
except ImportError:
    widget_axis = sys.modules[
        'datadog_api_client.v1.model.widget_axis']
try:
    from datadog_api_client.v1.model import widget_event
except ImportError:
    widget_event = sys.modules[
        'datadog_api_client.v1.model.widget_event']
try:
    from datadog_api_client.v1.model import widget_legend_size
except ImportError:
    widget_legend_size = sys.modules[
        'datadog_api_client.v1.model.widget_legend_size']
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules[
        'datadog_api_client.v1.model.widget_text_align']
try:
    from datadog_api_client.v1.model import widget_time
except ImportError:
    widget_time = sys.modules[
        'datadog_api_client.v1.model.widget_time']
from datadog_api_client.v1.model.heat_map_widget_definition import HeatMapWidgetDefinition


class TestHeatMapWidgetDefinition(unittest.TestCase):
    """HeatMapWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHeatMapWidgetDefinition(self):
        """Test HeatMapWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HeatMapWidgetDefinition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
