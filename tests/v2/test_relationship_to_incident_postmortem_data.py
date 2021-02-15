# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_postmortem_type import IncidentPostmortemType

globals()["IncidentPostmortemType"] = IncidentPostmortemType
from datadog_api_client.v2.model.relationship_to_incident_postmortem_data import RelationshipToIncidentPostmortemData


class TestRelationshipToIncidentPostmortemData(unittest.TestCase):
    """RelationshipToIncidentPostmortemData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRelationshipToIncidentPostmortemData(self):
        """Test RelationshipToIncidentPostmortemData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RelationshipToIncidentPostmortemData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
