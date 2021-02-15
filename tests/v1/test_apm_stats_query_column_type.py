# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.table_widget_cell_display_mode import TableWidgetCellDisplayMode
from datadog_api_client.v1.model.widget_sort import WidgetSort

globals()["TableWidgetCellDisplayMode"] = TableWidgetCellDisplayMode
globals()["WidgetSort"] = WidgetSort
from datadog_api_client.v1.model.apm_stats_query_column_type import ApmStatsQueryColumnType


class TestApmStatsQueryColumnType(unittest.TestCase):
    """ApmStatsQueryColumnType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApmStatsQueryColumnType(self):
        """Test ApmStatsQueryColumnType"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApmStatsQueryColumnType()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
