# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import access_role
except ImportError:
    access_role = sys.modules["datadog_api_client.v1.model.access_role"]
from datadog_api_client.v1.model.user import User


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        """Test User"""
        # FIXME: construct object with mandatory attributes with example values
        # model = User()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
