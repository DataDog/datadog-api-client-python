# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.dashboard_list_item_response import DashboardListItemResponse

globals()["DashboardListItemResponse"] = DashboardListItemResponse
from datadog_api_client.v2.model.dashboard_list_update_items_response import DashboardListUpdateItemsResponse


class TestDashboardListUpdateItemsResponse(unittest.TestCase):
    """DashboardListUpdateItemsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardListUpdateItemsResponse(self):
        """Test DashboardListUpdateItemsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardListUpdateItemsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
