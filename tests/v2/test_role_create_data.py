# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.role_create_attributes import RoleCreateAttributes
from datadog_api_client.v2.model.role_relationships import RoleRelationships
from datadog_api_client.v2.model.roles_type import RolesType

globals()["RoleCreateAttributes"] = RoleCreateAttributes
globals()["RoleRelationships"] = RoleRelationships
globals()["RolesType"] = RolesType
from datadog_api_client.v2.model.role_create_data import RoleCreateData


class TestRoleCreateData(unittest.TestCase):
    """RoleCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleCreateData(self):
        """Test RoleCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleCreateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
