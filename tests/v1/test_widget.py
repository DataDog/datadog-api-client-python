# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.widget_definition import WidgetDefinition
from datadog_api_client.v1.model.widget_layout import WidgetLayout

globals()["WidgetDefinition"] = WidgetDefinition
globals()["WidgetLayout"] = WidgetLayout
from datadog_api_client.v1.model.widget import Widget


class TestWidget(unittest.TestCase):
    """Widget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidget(self):
        """Test Widget"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Widget()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
