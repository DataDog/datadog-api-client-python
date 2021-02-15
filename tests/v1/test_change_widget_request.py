# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
from datadog_api_client.v1.model.widget_change_type import WidgetChangeType
from datadog_api_client.v1.model.widget_compare_to import WidgetCompareTo
from datadog_api_client.v1.model.widget_order_by import WidgetOrderBy
from datadog_api_client.v1.model.widget_sort import WidgetSort

globals()["LogQueryDefinition"] = LogQueryDefinition
globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
globals()["WidgetChangeType"] = WidgetChangeType
globals()["WidgetCompareTo"] = WidgetCompareTo
globals()["WidgetOrderBy"] = WidgetOrderBy
globals()["WidgetSort"] = WidgetSort
from datadog_api_client.v1.model.change_widget_request import ChangeWidgetRequest


class TestChangeWidgetRequest(unittest.TestCase):
    """ChangeWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangeWidgetRequest(self):
        """Test ChangeWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChangeWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
