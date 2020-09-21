# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.service_included_items import ServiceIncludedItems
from datadog_api_client.v2.model.service_response_data import ServiceResponseData
globals()['ServiceIncludedItems'] = ServiceIncludedItems
globals()['ServiceResponseData'] = ServiceResponseData
from datadog_api_client.v2.model.service_response import ServiceResponse


class TestServiceResponse(unittest.TestCase):
    """ServiceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceResponse(self):
        """Test ServiceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
