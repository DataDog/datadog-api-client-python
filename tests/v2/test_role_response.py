# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.role import Role

globals()["Role"] = Role
from datadog_api_client.v2.model.role_response import RoleResponse


class TestRoleResponse(unittest.TestCase):
    """RoleResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleResponse(self):
        """Test RoleResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
