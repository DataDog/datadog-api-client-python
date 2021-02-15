# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user_create_attributes import UserCreateAttributes
from datadog_api_client.v2.model.user_relationships import UserRelationships
from datadog_api_client.v2.model.users_type import UsersType

globals()["UserCreateAttributes"] = UserCreateAttributes
globals()["UserRelationships"] = UserRelationships
globals()["UsersType"] = UsersType
from datadog_api_client.v2.model.user_create_data import UserCreateData


class TestUserCreateData(unittest.TestCase):
    """UserCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserCreateData(self):
        """Test UserCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserCreateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
