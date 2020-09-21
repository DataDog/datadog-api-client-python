# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.team_create_attributes import TeamCreateAttributes
from datadog_api_client.v2.model.team_relationships import TeamRelationships
from datadog_api_client.v2.model.team_type import TeamType
globals()['TeamCreateAttributes'] = TeamCreateAttributes
globals()['TeamRelationships'] = TeamRelationships
globals()['TeamType'] = TeamType
from datadog_api_client.v2.model.team_create_data import TeamCreateData


class TestTeamCreateData(unittest.TestCase):
    """TeamCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamCreateData(self):
        """Test TeamCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TeamCreateData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
