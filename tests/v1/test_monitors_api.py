# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.monitors_api import MonitorsApi  # noqa: E501


class TestMonitorsApi(unittest.TestCase):
    """MonitorsApi unit test stubs"""

    def setUp(self):
        self.api = MonitorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_can_delete_monitor(self):
        """Test case for check_can_delete_monitor

        Check if a monitor can be deleted  # noqa: E501
        """
        pass

    def test_create_monitor(self):
        """Test case for create_monitor

        Create a monitor  # noqa: E501
        """
        pass

    def test_delete_monitor(self):
        """Test case for delete_monitor

        Delete a monitor  # noqa: E501
        """
        pass

    def test_get_monitor(self):
        """Test case for get_monitor

        Get a monitor's details  # noqa: E501
        """
        pass

    def test_list_monitors(self):
        """Test case for list_monitors

        Get all monitor details  # noqa: E501
        """
        pass

    def test_update_monitor(self):
        """Test case for update_monitor

        Edit a monitor  # noqa: E501
        """
        pass

    def test_validate_monitor(self):
        """Test case for validate_monitor

        Validate a monitor  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
