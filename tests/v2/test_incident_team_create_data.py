# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_team_create_attributes import IncidentTeamCreateAttributes
from datadog_api_client.v2.model.incident_team_relationships import IncidentTeamRelationships
from datadog_api_client.v2.model.incident_team_type import IncidentTeamType
globals()['IncidentTeamCreateAttributes'] = IncidentTeamCreateAttributes
globals()['IncidentTeamRelationships'] = IncidentTeamRelationships
globals()['IncidentTeamType'] = IncidentTeamType
from datadog_api_client.v2.model.incident_team_create_data import IncidentTeamCreateData


class TestIncidentTeamCreateData(unittest.TestCase):
    """IncidentTeamCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentTeamCreateData(self):
        """Test IncidentTeamCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentTeamCreateData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
