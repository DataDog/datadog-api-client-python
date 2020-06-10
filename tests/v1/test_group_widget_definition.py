# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import group_widget_definition_type
except ImportError:
    group_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.group_widget_definition_type']
try:
    from datadog_api_client.v1.model import widget
except ImportError:
    widget = sys.modules[
        'datadog_api_client.v1.model.widget']
try:
    from datadog_api_client.v1.model import widget_layout_type
except ImportError:
    widget_layout_type = sys.modules[
        'datadog_api_client.v1.model.widget_layout_type']
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


if __name__ == '__main__':
    unittest.main()
