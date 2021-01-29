# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_create_attributes import IncidentCreateAttributes
from datadog_api_client.v2.model.incident_create_relationships import IncidentCreateRelationships
from datadog_api_client.v2.model.incident_type import IncidentType

globals()["IncidentCreateAttributes"] = IncidentCreateAttributes
globals()["IncidentCreateRelationships"] = IncidentCreateRelationships
globals()["IncidentType"] = IncidentType
from datadog_api_client.v2.model.incident_create_data import IncidentCreateData


class TestIncidentCreateData(unittest.TestCase):
    """IncidentCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentCreateData(self):
        """Test IncidentCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentCreateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
