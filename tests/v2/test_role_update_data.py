# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.role_update_attributes import RoleUpdateAttributes
from datadog_api_client.v2.model.roles_type import RolesType

globals()["RoleUpdateAttributes"] = RoleUpdateAttributes
globals()["RolesType"] = RolesType
from datadog_api_client.v2.model.role_update_data import RoleUpdateData


class TestRoleUpdateData(unittest.TestCase):
    """RoleUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleUpdateData(self):
        """Test RoleUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
