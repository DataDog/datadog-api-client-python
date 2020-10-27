# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_service_included_items import IncidentServiceIncludedItems
from datadog_api_client.v2.model.incident_service_response_data import IncidentServiceResponseData
from datadog_api_client.v2.model.incident_services_response_meta import IncidentServicesResponseMeta
globals()['IncidentServiceIncludedItems'] = IncidentServiceIncludedItems
globals()['IncidentServiceResponseData'] = IncidentServiceResponseData
globals()['IncidentServicesResponseMeta'] = IncidentServicesResponseMeta
from datadog_api_client.v2.model.incident_services_response import IncidentServicesResponse


class TestIncidentServicesResponse(unittest.TestCase):
    """IncidentServicesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentServicesResponse(self):
        """Test IncidentServicesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentServicesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
