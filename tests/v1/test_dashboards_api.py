# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.dashboards_api import DashboardsApi  # noqa: E501


class TestDashboardsApi(unittest.TestCase):
    """DashboardsApi unit test stubs"""

    def setUp(self):
        self.api = DashboardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_dashboard(self):
        """Test case for create_dashboard

        Create a new dashboard  # noqa: E501
        """
        pass

    def test_delete_dashboard(self):
        """Test case for delete_dashboard

        Delete a dashboard  # noqa: E501
        """
        pass

    def test_get_dashboard(self):
        """Test case for get_dashboard

        Get a dashboard  # noqa: E501
        """
        pass

    def test_list_dashboards(self):
        """Test case for list_dashboards

        Get all dashboards  # noqa: E501
        """
        pass

    def test_update_dashboard(self):
        """Test case for update_dashboard

        Update a dashboard  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
