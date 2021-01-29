# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import dashboard_list_item_request
except ImportError:
    dashboard_list_item_request = sys.modules["datadog_api_client.v2.model.dashboard_list_item_request"]
from datadog_api_client.v2.model.dashboard_list_add_items_request import DashboardListAddItemsRequest


class TestDashboardListAddItemsRequest(unittest.TestCase):
    """DashboardListAddItemsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardListAddItemsRequest(self):
        """Test DashboardListAddItemsRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardListAddItemsRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
