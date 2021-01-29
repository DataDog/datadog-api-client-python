# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_response_attributes import IncidentResponseAttributes
from datadog_api_client.v2.model.incident_response_relationships import IncidentResponseRelationships
from datadog_api_client.v2.model.incident_type import IncidentType

globals()["IncidentResponseAttributes"] = IncidentResponseAttributes
globals()["IncidentResponseRelationships"] = IncidentResponseRelationships
globals()["IncidentType"] = IncidentType
from datadog_api_client.v2.model.incident_response_data import IncidentResponseData


class TestIncidentResponseData(unittest.TestCase):
    """IncidentResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentResponseData(self):
        """Test IncidentResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentResponseData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
