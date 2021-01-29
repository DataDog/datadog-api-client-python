# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.roles_api import RolesApi  # noqa: E501


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_permission_to_role(self):
        """Test case for add_permission_to_role

        Grant permission to a role  # noqa: E501
        """
        pass

    def test_add_user_to_role(self):
        """Test case for add_user_to_role

        Add a user to a role  # noqa: E501
        """
        pass

    def test_create_role(self):
        """Test case for create_role

        Create role  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete role  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get a role  # noqa: E501
        """
        pass

    def test_list_permissions(self):
        """Test case for list_permissions

        List permissions  # noqa: E501
        """
        pass

    def test_list_role_permissions(self):
        """Test case for list_role_permissions

        List permissions for a role  # noqa: E501
        """
        pass

    def test_list_role_users(self):
        """Test case for list_role_users

        Get all users of a role  # noqa: E501
        """
        pass

    def test_list_roles(self):
        """Test case for list_roles

        List roles  # noqa: E501
        """
        pass

    def test_remove_permission_from_role(self):
        """Test case for remove_permission_from_role

        Revoke permission  # noqa: E501
        """
        pass

    def test_remove_user_from_role(self):
        """Test case for remove_user_from_role

        Remove a user from a role  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update a role  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
