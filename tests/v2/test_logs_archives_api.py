# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi  # noqa: E501


class TestLogsArchivesApi(unittest.TestCase):
    """LogsArchivesApi unit test stubs"""

    def setUp(self):
        self.api = LogsArchivesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_read_role_to_archive(self):
        """Test case for add_read_role_to_archive

        Grant role to an archive  # noqa: E501
        """
        pass

    def test_create_logs_archive(self):
        """Test case for create_logs_archive

        Create an archive  # noqa: E501
        """
        pass

    def test_delete_logs_archive(self):
        """Test case for delete_logs_archive

        Delete an archive  # noqa: E501
        """
        pass

    def test_get_logs_archive(self):
        """Test case for get_logs_archive

        Get an archive  # noqa: E501
        """
        pass

    def test_list_archive_read_roles(self):
        """Test case for list_archive_read_roles

        List read roles for an archive  # noqa: E501
        """
        pass

    def test_list_logs_archives(self):
        """Test case for list_logs_archives

        Get all archives  # noqa: E501
        """
        pass

    def test_remove_role_from_archive(self):
        """Test case for remove_role_from_archive

        Revoke role from an archive  # noqa: E501
        """
        pass

    def test_update_logs_archive(self):
        """Test case for update_logs_archive

        Update an archive  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
