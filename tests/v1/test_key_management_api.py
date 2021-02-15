# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.key_management_api import KeyManagementApi  # noqa: E501


class TestKeyManagementApi(unittest.TestCase):
    """KeyManagementApi unit test stubs"""

    def setUp(self):
        self.api = KeyManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_key(self):
        """Test case for create_api_key

        Create an API key  # noqa: E501
        """
        pass

    def test_create_application_key(self):
        """Test case for create_application_key

        Create an application key  # noqa: E501
        """
        pass

    def test_delete_api_key(self):
        """Test case for delete_api_key

        Delete an API key  # noqa: E501
        """
        pass

    def test_delete_application_key(self):
        """Test case for delete_application_key

        Delete an application key  # noqa: E501
        """
        pass

    def test_get_api_key(self):
        """Test case for get_api_key

        Get API key  # noqa: E501
        """
        pass

    def test_get_application_key(self):
        """Test case for get_application_key

        Get an application key  # noqa: E501
        """
        pass

    def test_list_api_keys(self):
        """Test case for list_api_keys

        Get all API keys  # noqa: E501
        """
        pass

    def test_list_application_keys(self):
        """Test case for list_application_keys

        Get all application keys  # noqa: E501
        """
        pass

    def test_update_api_key(self):
        """Test case for update_api_key

        Edit an API key  # noqa: E501
        """
        pass

    def test_update_application_key(self):
        """Test case for update_application_key

        Edit an application key  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
