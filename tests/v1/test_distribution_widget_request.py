# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
from datadog_api_client.v1.model.widget_style import WidgetStyle

globals()["LogQueryDefinition"] = LogQueryDefinition
globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
globals()["WidgetStyle"] = WidgetStyle
from datadog_api_client.v1.model.distribution_widget_request import DistributionWidgetRequest


class TestDistributionWidgetRequest(unittest.TestCase):
    """DistributionWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDistributionWidgetRequest(self):
        """Test DistributionWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DistributionWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
