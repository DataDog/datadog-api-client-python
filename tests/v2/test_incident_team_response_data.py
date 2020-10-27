# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_team_relationships import IncidentTeamRelationships
from datadog_api_client.v2.model.incident_team_response_attributes import IncidentTeamResponseAttributes
from datadog_api_client.v2.model.incident_team_type import IncidentTeamType
globals()['IncidentTeamRelationships'] = IncidentTeamRelationships
globals()['IncidentTeamResponseAttributes'] = IncidentTeamResponseAttributes
globals()['IncidentTeamType'] = IncidentTeamType
from datadog_api_client.v2.model.incident_team_response_data import IncidentTeamResponseData


class TestIncidentTeamResponseData(unittest.TestCase):
    """IncidentTeamResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentTeamResponseData(self):
        """Test IncidentTeamResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentTeamResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
