# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import widget_live_span
except ImportError:
    widget_live_span = sys.modules[
        'datadog_api_client.v1.model.widget_live_span']
from datadog_api_client.v1.model.widget_time import WidgetTime


class TestWidgetTime(unittest.TestCase):
    """WidgetTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetTime(self):
        """Test WidgetTime"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WidgetTime()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
