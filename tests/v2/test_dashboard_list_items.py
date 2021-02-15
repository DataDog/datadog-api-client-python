# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.dashboard_list_item import DashboardListItem

globals()["DashboardListItem"] = DashboardListItem
from datadog_api_client.v2.model.dashboard_list_items import DashboardListItems


class TestDashboardListItems(unittest.TestCase):
    """DashboardListItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardListItems(self):
        """Test DashboardListItems"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardListItems()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
