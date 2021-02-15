# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.relationship_to_organization import RelationshipToOrganization
from datadog_api_client.v2.model.relationship_to_organizations import RelationshipToOrganizations
from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles
from datadog_api_client.v2.model.relationship_to_users import RelationshipToUsers

globals()["RelationshipToOrganization"] = RelationshipToOrganization
globals()["RelationshipToOrganizations"] = RelationshipToOrganizations
globals()["RelationshipToRoles"] = RelationshipToRoles
globals()["RelationshipToUsers"] = RelationshipToUsers
from datadog_api_client.v2.model.user_response_relationships import UserResponseRelationships


class TestUserResponseRelationships(unittest.TestCase):
    """UserResponseRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserResponseRelationships(self):
        """Test UserResponseRelationships"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserResponseRelationships()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
