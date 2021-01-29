# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a user  # noqa: E501
        """
        pass

    def test_disable_user(self):
        """Test case for disable_user

        Disable a user  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user details  # noqa: E501
        """
        pass

    def test_list_users(self):
        """Test case for list_users

        Get all users  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Update a user  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
