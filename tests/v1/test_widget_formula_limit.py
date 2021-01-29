# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.query_sort_order import QuerySortOrder

globals()["QuerySortOrder"] = QuerySortOrder
from datadog_api_client.v1.model.widget_formula_limit import WidgetFormulaLimit


class TestWidgetFormulaLimit(unittest.TestCase):
    """WidgetFormulaLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetFormulaLimit(self):
        """Test WidgetFormulaLimit"""
        # FIXME: construct object with mandatory attributes with example values
        # model = WidgetFormulaLimit()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
