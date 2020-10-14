# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.services_response_meta import ServicesResponseMeta
from datadog_api_client.v2.model.team_included_items import TeamIncludedItems
from datadog_api_client.v2.model.team_response_data import TeamResponseData
globals()['ServicesResponseMeta'] = ServicesResponseMeta
globals()['TeamIncludedItems'] = TeamIncludedItems
globals()['TeamResponseData'] = TeamResponseData
from datadog_api_client.v2.model.teams_response import TeamsResponse


class TestTeamsResponse(unittest.TestCase):
    """TeamsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamsResponse(self):
        """Test TeamsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TeamsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
