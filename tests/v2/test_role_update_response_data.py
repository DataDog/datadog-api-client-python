# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes
from datadog_api_client.v2.model.roles_type import RolesType

globals()["RoleResponseRelationships"] = RoleResponseRelationships
globals()["RoleUpdateAttributes"] = RoleUpdateAttributes
globals()["RolesType"] = RolesType
from datadog_api_client.v2.model.role_update_response_data import RoleUpdateResponseData


class TestRoleUpdateResponseData(unittest.TestCase):
    """RoleUpdateResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleUpdateResponseData(self):
        """Test RoleUpdateResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleUpdateResponseData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
