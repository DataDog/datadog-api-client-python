# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser

globals()["RelationshipToUser"] = RelationshipToUser
from datadog_api_client.v2.model.incident_create_relationships import IncidentCreateRelationships


class TestIncidentCreateRelationships(unittest.TestCase):
    """IncidentCreateRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentCreateRelationships(self):
        """Test IncidentCreateRelationships"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentCreateRelationships()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
