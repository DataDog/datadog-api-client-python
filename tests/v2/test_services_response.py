# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.service_included_items import ServiceIncludedItems
from datadog_api_client.v2.model.service_response_data import ServiceResponseData
from datadog_api_client.v2.model.services_response_meta import ServicesResponseMeta
globals()['ServiceIncludedItems'] = ServiceIncludedItems
globals()['ServiceResponseData'] = ServiceResponseData
globals()['ServicesResponseMeta'] = ServicesResponseMeta
from datadog_api_client.v2.model.services_response import ServicesResponse


class TestServicesResponse(unittest.TestCase):
    """ServicesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServicesResponse(self):
        """Test ServicesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServicesResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
