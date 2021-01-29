# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles

globals()["RelationshipToRoles"] = RelationshipToRoles
from datadog_api_client.v2.model.user_relationships import UserRelationships


class TestUserRelationships(unittest.TestCase):
    """UserRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserRelationships(self):
        """Test UserRelationships"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserRelationships()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
