# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_service_create_attributes import IncidentServiceCreateAttributes
from datadog_api_client.v2.model.incident_service_relationships import IncidentServiceRelationships
from datadog_api_client.v2.model.incident_service_type import IncidentServiceType
globals()['IncidentServiceCreateAttributes'] = IncidentServiceCreateAttributes
globals()['IncidentServiceRelationships'] = IncidentServiceRelationships
globals()['IncidentServiceType'] = IncidentServiceType
from datadog_api_client.v2.model.incident_service_create_data import IncidentServiceCreateData


class TestIncidentServiceCreateData(unittest.TestCase):
    """IncidentServiceCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentServiceCreateData(self):
        """Test IncidentServiceCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentServiceCreateData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
