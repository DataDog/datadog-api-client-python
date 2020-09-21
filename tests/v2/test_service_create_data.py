# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.service_create_attributes import ServiceCreateAttributes
from datadog_api_client.v2.model.service_relationships import ServiceRelationships
from datadog_api_client.v2.model.service_type import ServiceType
globals()['ServiceCreateAttributes'] = ServiceCreateAttributes
globals()['ServiceRelationships'] = ServiceRelationships
globals()['ServiceType'] = ServiceType
from datadog_api_client.v2.model.service_create_data import ServiceCreateData


class TestServiceCreateData(unittest.TestCase):
    """ServiceCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceCreateData(self):
        """Test ServiceCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceCreateData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
