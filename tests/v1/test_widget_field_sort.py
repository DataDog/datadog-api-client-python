# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.widget_sort import WidgetSort

globals()["WidgetSort"] = WidgetSort
from datadog_api_client.v1.model.widget_field_sort import WidgetFieldSort


class TestWidgetFieldSort(unittest.TestCase):
    """WidgetFieldSort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetFieldSort(self):
        """Test WidgetFieldSort"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WidgetFieldSort()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
