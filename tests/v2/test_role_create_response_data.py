# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.role_create_attributes import RoleCreateAttributes
from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
from datadog_api_client.v2.model.roles_type import RolesType

globals()["RoleCreateAttributes"] = RoleCreateAttributes
globals()["RoleResponseRelationships"] = RoleResponseRelationships
globals()["RolesType"] = RolesType
from datadog_api_client.v2.model.role_create_response_data import RoleCreateResponseData


class TestRoleCreateResponseData(unittest.TestCase):
    """RoleCreateResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleCreateResponseData(self):
        """Test RoleCreateResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleCreateResponseData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
