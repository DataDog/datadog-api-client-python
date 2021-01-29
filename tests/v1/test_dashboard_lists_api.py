# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi  # noqa: E501


class TestDashboardListsApi(unittest.TestCase):
    """DashboardListsApi unit test stubs"""

    def setUp(self):
        self.api = DashboardListsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_dashboard_list(self):
        """Test case for create_dashboard_list

        Create a dashboard list  # noqa: E501
        """
        pass

    def test_delete_dashboard_list(self):
        """Test case for delete_dashboard_list

        Delete a dashboard list  # noqa: E501
        """
        pass

    def test_get_dashboard_list(self):
        """Test case for get_dashboard_list

        Get a dashboard list  # noqa: E501
        """
        pass

    def test_list_dashboard_lists(self):
        """Test case for list_dashboard_lists

        Get all dashboard lists  # noqa: E501
        """
        pass

    def test_update_dashboard_list(self):
        """Test case for update_dashboard_list

        Update a dashboard list  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
