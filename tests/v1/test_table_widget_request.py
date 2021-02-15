# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.apm_stats_query_definition import ApmStatsQueryDefinition
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
from datadog_api_client.v1.model.table_widget_cell_display_mode import TableWidgetCellDisplayMode
from datadog_api_client.v1.model.widget_aggregator import WidgetAggregator
from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
from datadog_api_client.v1.model.widget_sort import WidgetSort

globals()["ApmStatsQueryDefinition"] = ApmStatsQueryDefinition
globals()["LogQueryDefinition"] = LogQueryDefinition
globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
globals()["TableWidgetCellDisplayMode"] = TableWidgetCellDisplayMode
globals()["WidgetAggregator"] = WidgetAggregator
globals()["WidgetConditionalFormat"] = WidgetConditionalFormat
globals()["WidgetSort"] = WidgetSort
from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest


class TestTableWidgetRequest(unittest.TestCase):
    """TableWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTableWidgetRequest(self):
        """Test TableWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TableWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
