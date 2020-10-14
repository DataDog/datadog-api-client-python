# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.service_update_data import ServiceUpdateData
globals()['ServiceUpdateData'] = ServiceUpdateData
from datadog_api_client.v2.model.service_update_request import ServiceUpdateRequest


class TestServiceUpdateRequest(unittest.TestCase):
    """ServiceUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceUpdateRequest(self):
        """Test ServiceUpdateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceUpdateRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
