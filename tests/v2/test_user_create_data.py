# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import user_create_attributes
except ImportError:
    user_create_attributes = sys.modules[
        'datadog_api_client.v2.model.user_create_attributes']
try:
    from datadog_api_client.v2.model import user_relationships
except ImportError:
    user_relationships = sys.modules[
        'datadog_api_client.v2.model.user_relationships']
try:
    from datadog_api_client.v2.model import users_type
except ImportError:
    users_type = sys.modules[
        'datadog_api_client.v2.model.users_type']
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


if __name__ == '__main__':
    unittest.main()
