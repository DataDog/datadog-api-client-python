# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi  # noqa: E501


class TestIncidentServicesApi(unittest.TestCase):
    """IncidentServicesApi unit test stubs"""

    def setUp(self):
        self.api = IncidentServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_incident_service(self):
        """Test case for create_incident_service

        Create a new incident service  # noqa: E501
        """
        pass

    def test_delete_incident_service(self):
        """Test case for delete_incident_service

        Delete an existing incident service  # noqa: E501
        """
        pass

    def test_get_incident_service(self):
        """Test case for get_incident_service

        Get details of an incident service  # noqa: E501
        """
        pass

    def test_get_incident_services(self):
        """Test case for get_incident_services

        Get a list of all incident services  # noqa: E501
        """
        pass

    def test_update_incident_service(self):
        """Test case for update_incident_service

        Update an existing incident service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
