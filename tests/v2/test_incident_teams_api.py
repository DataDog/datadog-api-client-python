# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.incident_teams_api import IncidentTeamsApi  # noqa: E501


class TestIncidentTeamsApi(unittest.TestCase):
    """IncidentTeamsApi unit test stubs"""

    def setUp(self):
        self.api = IncidentTeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_incident_team(self):
        """Test case for create_incident_team

        Create a new incident team  # noqa: E501
        """
        pass

    def test_delete_incident_team(self):
        """Test case for delete_incident_team

        Delete an existing incident team  # noqa: E501
        """
        pass

    def test_get_incident_team(self):
        """Test case for get_incident_team

        Get details of an incident team  # noqa: E501
        """
        pass

    def test_get_incident_teams(self):
        """Test case for get_incident_teams

        Get a list of all incident teams  # noqa: E501
        """
        pass

    def test_update_incident_team(self):
        """Test case for update_incident_team

        Update an existing incident team  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
