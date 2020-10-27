# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_team_update_data import IncidentTeamUpdateData
globals()['IncidentTeamUpdateData'] = IncidentTeamUpdateData
from datadog_api_client.v2.model.incident_team_update_request import IncidentTeamUpdateRequest


class TestIncidentTeamUpdateRequest(unittest.TestCase):
    """IncidentTeamUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentTeamUpdateRequest(self):
        """Test IncidentTeamUpdateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentTeamUpdateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
