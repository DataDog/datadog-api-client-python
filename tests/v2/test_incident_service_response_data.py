# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_service_relationships import IncidentServiceRelationships
from datadog_api_client.v2.model.incident_service_response_attributes import IncidentServiceResponseAttributes
from datadog_api_client.v2.model.incident_service_type import IncidentServiceType
globals()['IncidentServiceRelationships'] = IncidentServiceRelationships
globals()['IncidentServiceResponseAttributes'] = IncidentServiceResponseAttributes
globals()['IncidentServiceType'] = IncidentServiceType
from datadog_api_client.v2.model.incident_service_response_data import IncidentServiceResponseData


class TestIncidentServiceResponseData(unittest.TestCase):
    """IncidentServiceResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentServiceResponseData(self):
        """Test IncidentServiceResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentServiceResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
