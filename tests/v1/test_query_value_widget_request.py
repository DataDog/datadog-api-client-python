# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
from datadog_api_client.v1.model.widget_aggregator import WidgetAggregator
from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat

globals()["LogQueryDefinition"] = LogQueryDefinition
globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
globals()["WidgetAggregator"] = WidgetAggregator
globals()["WidgetConditionalFormat"] = WidgetConditionalFormat
from datadog_api_client.v1.model.query_value_widget_request import QueryValueWidgetRequest


class TestQueryValueWidgetRequest(unittest.TestCase):
    """QueryValueWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQueryValueWidgetRequest(self):
        """Test QueryValueWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QueryValueWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
