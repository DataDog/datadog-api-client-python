# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user_relationship_data import UserRelationshipData
globals()['UserRelationshipData'] = UserRelationshipData
from datadog_api_client.v2.model.user_relationship import UserRelationship


class TestUserRelationship(unittest.TestCase):
    """UserRelationship unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserRelationship(self):
        """Test UserRelationship"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserRelationship()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
