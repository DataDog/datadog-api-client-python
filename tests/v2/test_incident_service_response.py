# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_service_included_items import IncidentServiceIncludedItems
from datadog_api_client.v2.model.incident_service_response_data import IncidentServiceResponseData
globals()['IncidentServiceIncludedItems'] = IncidentServiceIncludedItems
globals()['IncidentServiceResponseData'] = IncidentServiceResponseData
from datadog_api_client.v2.model.incident_service_response import IncidentServiceResponse


class TestIncidentServiceResponse(unittest.TestCase):
    """IncidentServiceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentServiceResponse(self):
        """Test IncidentServiceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentServiceResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
