# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.service_create_data import ServiceCreateData
globals()['ServiceCreateData'] = ServiceCreateData
from datadog_api_client.v2.model.service_create_request import ServiceCreateRequest


class TestServiceCreateRequest(unittest.TestCase):
    """ServiceCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceCreateRequest(self):
        """Test ServiceCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceCreateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
