# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
globals()['RelationshipToUser'] = RelationshipToUser
from datadog_api_client.v2.model.application_key_relationships import ApplicationKeyRelationships


class TestApplicationKeyRelationships(unittest.TestCase):
    """ApplicationKeyRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationKeyRelationships(self):
        """Test ApplicationKeyRelationships"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationKeyRelationships()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
