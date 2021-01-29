# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.role import Role
from datadog_api_client.v2.model.role_attributes import RoleAttributes
from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
from datadog_api_client.v2.model.roles_type import RolesType
from datadog_api_client.v2.model.user import User

globals()["Role"] = Role
globals()["RoleAttributes"] = RoleAttributes
globals()["RoleResponseRelationships"] = RoleResponseRelationships
globals()["RolesType"] = RolesType
globals()["User"] = User
from datadog_api_client.v2.model.application_key_response_included_item import ApplicationKeyResponseIncludedItem


class TestApplicationKeyResponseIncludedItem(unittest.TestCase):
    """ApplicationKeyResponseIncludedItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationKeyResponseIncludedItem(self):
        """Test ApplicationKeyResponseIncludedItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationKeyResponseIncludedItem()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
