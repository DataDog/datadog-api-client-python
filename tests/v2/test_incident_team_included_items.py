# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user import User
from datadog_api_client.v2.model.user_attributes import UserAttributes
from datadog_api_client.v2.model.user_response_relationships import UserResponseRelationships
from datadog_api_client.v2.model.users_type import UsersType
globals()['User'] = User
globals()['UserAttributes'] = UserAttributes
globals()['UserResponseRelationships'] = UserResponseRelationships
globals()['UsersType'] = UsersType
from datadog_api_client.v2.model.incident_team_included_items import IncidentTeamIncludedItems


class TestIncidentTeamIncludedItems(unittest.TestCase):
    """IncidentTeamIncludedItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentTeamIncludedItems(self):
        """Test IncidentTeamIncludedItems"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentTeamIncludedItems()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
