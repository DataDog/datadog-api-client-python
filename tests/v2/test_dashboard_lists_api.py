# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.dashboard_lists_api import DashboardListsApi  # noqa: E501


class TestDashboardListsApi(unittest.TestCase):
    """DashboardListsApi unit test stubs"""

    def setUp(self):
        self.api = DashboardListsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_dashboard_list_items(self):
        """Test case for create_dashboard_list_items

        Add Items to a Dashboard List  # noqa: E501
        """
        pass

    def test_delete_dashboard_list_items(self):
        """Test case for delete_dashboard_list_items

        Delete items from a dashboard list  # noqa: E501
        """
        pass

    def test_get_dashboard_list_items(self):
        """Test case for get_dashboard_list_items

        Get items of a Dashboard List  # noqa: E501
        """
        pass

    def test_update_dashboard_list_items(self):
        """Test case for update_dashboard_list_items

        Update items of a dashboard list  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
