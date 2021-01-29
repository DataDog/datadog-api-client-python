# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import relationship_to_organization
except ImportError:
    relationship_to_organization = sys.modules["datadog_api_client.v2.model.relationship_to_organization"]
try:
    from datadog_api_client.v2.model import relationship_to_organizations
except ImportError:
    relationship_to_organizations = sys.modules["datadog_api_client.v2.model.relationship_to_organizations"]
try:
    from datadog_api_client.v2.model import relationship_to_roles
except ImportError:
    relationship_to_roles = sys.modules["datadog_api_client.v2.model.relationship_to_roles"]
try:
    from datadog_api_client.v2.model import relationship_to_users
except ImportError:
    relationship_to_users = sys.modules["datadog_api_client.v2.model.relationship_to_users"]
from datadog_api_client.v2.model.user_response_relationships import UserResponseRelationships


class TestUserResponseRelationships(unittest.TestCase):
    """UserResponseRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserResponseRelationships(self):
        """Test UserResponseRelationships"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserResponseRelationships()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
