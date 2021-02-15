# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user_update_attributes import UserUpdateAttributes
from datadog_api_client.v2.model.users_type import UsersType

globals()["UserUpdateAttributes"] = UserUpdateAttributes
globals()["UsersType"] = UsersType
from datadog_api_client.v2.model.user_update_data import UserUpdateData


class TestUserUpdateData(unittest.TestCase):
    """UserUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserUpdateData(self):
        """Test UserUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
