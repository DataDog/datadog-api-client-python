# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi  # noqa: E501


class TestSyntheticsApi(unittest.TestCase):
    """SyntheticsApi unit test stubs"""

    def setUp(self):
        self.api = SyntheticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_test(self):
        """Test case for create_test

        Create a test  # noqa: E501
        """
        pass

    def test_delete_tests(self):
        """Test case for delete_tests

        Delete tests  # noqa: E501
        """
        pass

    def test_get_api_test_latest_results(self):
        """Test case for get_api_test_latest_results

        Get the test's latest results summaries (API)  # noqa: E501
        """
        pass

    def test_get_api_test_result(self):
        """Test case for get_api_test_result

        Get a test result (API)  # noqa: E501
        """
        pass

    def test_get_browser_test(self):
        """Test case for get_browser_test

        Get a test configuration (browser)  # noqa: E501
        """
        pass

    def test_get_browser_test_latest_results(self):
        """Test case for get_browser_test_latest_results

        Get the test's latest results summaries (browser)  # noqa: E501
        """
        pass

    def test_get_browser_test_result(self):
        """Test case for get_browser_test_result

        Get a test result (browser)  # noqa: E501
        """
        pass

    def test_get_test(self):
        """Test case for get_test

        Get a test configuration (API)  # noqa: E501
        """
        pass

    def test_list_locations(self):
        """Test case for list_locations

        Get all locations (public and private)  # noqa: E501
        """
        pass

    def test_list_tests(self):
        """Test case for list_tests

        Get a list of tests  # noqa: E501
        """
        pass

    def test_update_test(self):
        """Test case for update_test

        Edit a test  # noqa: E501
        """
        pass

    def test_update_test_pause_status(self):
        """Test case for update_test_pause_status

        Pause or start a test  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
