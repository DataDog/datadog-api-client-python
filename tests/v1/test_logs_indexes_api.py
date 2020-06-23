# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.logs_indexes_api import LogsIndexesApi  # noqa: E501


class TestLogsIndexesApi(unittest.TestCase):
    """LogsIndexesApi unit test stubs"""

    def setUp(self):
        self.api = LogsIndexesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_logs_index(self):
        """Test case for get_logs_index

        Get an index  # noqa: E501
        """
        pass

    def test_get_logs_index_order(self):
        """Test case for get_logs_index_order

        Get indexes order  # noqa: E501
        """
        pass

    def test_list_log_indexes(self):
        """Test case for list_log_indexes

        Get all indexes  # noqa: E501
        """
        pass

    def test_update_logs_index(self):
        """Test case for update_logs_index

        Update an index  # noqa: E501
        """
        pass

    def test_update_logs_index_order(self):
        """Test case for update_logs_index_order

        Update indexes order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
