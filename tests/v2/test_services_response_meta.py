# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.services_response_meta_pagination import ServicesResponseMetaPagination
globals()['ServicesResponseMetaPagination'] = ServicesResponseMetaPagination
from datadog_api_client.v2.model.services_response_meta import ServicesResponseMeta


class TestServicesResponseMeta(unittest.TestCase):
    """ServicesResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServicesResponseMeta(self):
        """Test ServicesResponseMeta"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServicesResponseMeta()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
