# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.processes_api import ProcessesApi  # noqa: E501


class TestProcessesApi(unittest.TestCase):
    """ProcessesApi unit test stubs"""

    def setUp(self):
        self.api = ProcessesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_processes(self):
        """Test case for list_processes

        Get all processes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
