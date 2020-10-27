# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_service_relationships import IncidentServiceRelationships
from datadog_api_client.v2.model.incident_service_type import IncidentServiceType
from datadog_api_client.v2.model.incident_service_update_attributes import IncidentServiceUpdateAttributes
globals()['IncidentServiceRelationships'] = IncidentServiceRelationships
globals()['IncidentServiceType'] = IncidentServiceType
globals()['IncidentServiceUpdateAttributes'] = IncidentServiceUpdateAttributes
from datadog_api_client.v2.model.incident_service_update_data import IncidentServiceUpdateData


class TestIncidentServiceUpdateData(unittest.TestCase):
    """IncidentServiceUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentServiceUpdateData(self):
        """Test IncidentServiceUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentServiceUpdateData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
