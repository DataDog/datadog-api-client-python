# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_team_create_data import IncidentTeamCreateData
globals()['IncidentTeamCreateData'] = IncidentTeamCreateData
from datadog_api_client.v2.model.incident_team_create_request import IncidentTeamCreateRequest


class TestIncidentTeamCreateRequest(unittest.TestCase):
    """IncidentTeamCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentTeamCreateRequest(self):
        """Test IncidentTeamCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentTeamCreateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
