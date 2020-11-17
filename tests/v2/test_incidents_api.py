# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.incidents_api import IncidentsApi  # noqa: E501


class TestIncidentsApi(unittest.TestCase):
    """IncidentsApi unit test stubs"""

    def setUp(self):
        self.api = IncidentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_incident(self):
        """Test case for create_incident

        Create an incident  # noqa: E501
        """
        pass

    def test_delete_incident(self):
        """Test case for delete_incident

        Delete an existing incident  # noqa: E501
        """
        pass

    def test_get_incident(self):
        """Test case for get_incident

        Get the details of an incident  # noqa: E501
        """
        pass

    def test_list_incidents(self):
        """Test case for list_incidents

        Get a list of incidents  # noqa: E501
        """
        pass

    def test_update_incident(self):
        """Test case for update_incident

        Update an existing incident  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
