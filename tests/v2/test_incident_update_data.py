# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.incident_update_attributes import IncidentUpdateAttributes
from datadog_api_client.v2.model.incident_update_relationships import IncidentUpdateRelationships

globals()["IncidentType"] = IncidentType
globals()["IncidentUpdateAttributes"] = IncidentUpdateAttributes
globals()["IncidentUpdateRelationships"] = IncidentUpdateRelationships
from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData


class TestIncidentUpdateData(unittest.TestCase):
    """IncidentUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentUpdateData(self):
        """Test IncidentUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
