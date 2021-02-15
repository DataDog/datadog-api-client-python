# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth

globals()["WidgetLineType"] = WidgetLineType
globals()["WidgetLineWidth"] = WidgetLineWidth
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle


class TestWidgetRequestStyle(unittest.TestCase):
    """WidgetRequestStyle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetRequestStyle(self):
        """Test WidgetRequestStyle"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WidgetRequestStyle()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
