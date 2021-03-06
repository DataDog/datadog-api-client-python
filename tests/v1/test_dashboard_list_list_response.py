# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.dashboard_list import DashboardList

globals()["DashboardList"] = DashboardList
from datadog_api_client.v1.model.dashboard_list_list_response import DashboardListListResponse


class TestDashboardListListResponse(unittest.TestCase):
    """DashboardListListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardListListResponse(self):
        """Test DashboardListListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardListListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
