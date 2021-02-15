# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.relationship_to_permissions import RelationshipToPermissions

globals()["RelationshipToPermissions"] = RelationshipToPermissions
from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships


class TestRoleResponseRelationships(unittest.TestCase):
    """RoleResponseRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleResponseRelationships(self):
        """Test RoleResponseRelationships"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleResponseRelationships()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
