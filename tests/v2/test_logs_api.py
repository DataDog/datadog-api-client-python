# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.logs_api import LogsApi  # noqa: E501


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self):
        self.api = LogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_logs(self):
        """Test case for list_logs

        Get a list of logs  # noqa: E501
        """
        pass

    def test_list_logs_get(self):
        """Test case for list_logs_get

        Get a quick list of logs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
