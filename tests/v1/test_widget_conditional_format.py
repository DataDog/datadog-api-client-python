# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import widget_comparator
except ImportError:
    widget_comparator = sys.modules["datadog_api_client.v1.model.widget_comparator"]
try:
    from datadog_api_client.v1.model import widget_palette
except ImportError:
    widget_palette = sys.modules["datadog_api_client.v1.model.widget_palette"]
from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat


class TestWidgetConditionalFormat(unittest.TestCase):
    """WidgetConditionalFormat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetConditionalFormat(self):
        """Test WidgetConditionalFormat"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WidgetConditionalFormat()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
