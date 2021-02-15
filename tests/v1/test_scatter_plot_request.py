# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
from datadog_api_client.v1.model.widget_aggregator import WidgetAggregator

globals()["LogQueryDefinition"] = LogQueryDefinition
globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
globals()["WidgetAggregator"] = WidgetAggregator
from datadog_api_client.v1.model.scatter_plot_request import ScatterPlotRequest


class TestScatterPlotRequest(unittest.TestCase):
    """ScatterPlotRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScatterPlotRequest(self):
        """Test ScatterPlotRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScatterPlotRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
