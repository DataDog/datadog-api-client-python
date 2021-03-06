# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.relationship_to_role_data import RelationshipToRoleData

globals()["RelationshipToRoleData"] = RelationshipToRoleData
from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles


class TestRelationshipToRoles(unittest.TestCase):
    """RelationshipToRoles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRelationshipToRoles(self):
        """Test RelationshipToRoles"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RelationshipToRoles()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
