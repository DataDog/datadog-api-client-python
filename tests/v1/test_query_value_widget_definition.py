# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import query_value_widget_definition_type
except ImportError:
    query_value_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.query_value_widget_definition_type']
try:
    from datadog_api_client.v1.model import query_value_widget_request
except ImportError:
    query_value_widget_request = sys.modules[
        'datadog_api_client.v1.model.query_value_widget_request']
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
from datadog_api_client.v1.model.query_value_widget_definition import QueryValueWidgetDefinition


class TestQueryValueWidgetDefinition(unittest.TestCase):
    """QueryValueWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQueryValueWidgetDefinition(self):
        """Test QueryValueWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QueryValueWidgetDefinition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
