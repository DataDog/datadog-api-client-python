# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.dashboard_summary_definition import DashboardSummaryDefinition

globals()["DashboardSummaryDefinition"] = DashboardSummaryDefinition
from datadog_api_client.v1.model.dashboard_summary import DashboardSummary


class TestDashboardSummary(unittest.TestCase):
    """DashboardSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardSummary(self):
        """Test DashboardSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardSummary()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
