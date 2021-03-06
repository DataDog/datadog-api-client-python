# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.dashboard_list_item_request import DashboardListItemRequest

globals()["DashboardListItemRequest"] = DashboardListItemRequest
from datadog_api_client.v2.model.dashboard_list_delete_items_request import DashboardListDeleteItemsRequest


class TestDashboardListDeleteItemsRequest(unittest.TestCase):
    """DashboardListDeleteItemsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardListDeleteItemsRequest(self):
        """Test DashboardListDeleteItemsRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardListDeleteItemsRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
