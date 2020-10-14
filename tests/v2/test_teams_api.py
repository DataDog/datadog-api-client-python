# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.teams_api import TeamsApi  # noqa: E501


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_team(self):
        """Test case for create_team

        Create a new team  # noqa: E501
        """
        pass

    def test_delete_team(self):
        """Test case for delete_team

        Delete an existing team  # noqa: E501
        """
        pass

    def test_get_team(self):
        """Test case for get_team

        Get details of a team  # noqa: E501
        """
        pass

    def test_get_teams(self):
        """Test case for get_teams

        Get a list of all teams  # noqa: E501
        """
        pass

    def test_update_team(self):
        """Test case for update_team

        Update an existing team  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
