# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.services_api import ServicesApi  # noqa: E501


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self):
        self.api = ServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service(self):
        """Test case for create_service

        Create a new service  # noqa: E501
        """
        pass

    def test_delete_service(self):
        """Test case for delete_service

        Delete an existing service  # noqa: E501
        """
        pass

    def test_get_service(self):
        """Test case for get_service

        Get details of a service  # noqa: E501
        """
        pass

    def test_get_services(self):
        """Test case for get_services

        Get a list of all services  # noqa: E501
        """
        pass

    def test_update_service(self):
        """Test case for update_service

        Update an existing service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
