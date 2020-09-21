# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.service_relationships import ServiceRelationships
from datadog_api_client.v2.model.service_type import ServiceType
from datadog_api_client.v2.model.service_update_attributes import ServiceUpdateAttributes
globals()['ServiceRelationships'] = ServiceRelationships
globals()['ServiceType'] = ServiceType
globals()['ServiceUpdateAttributes'] = ServiceUpdateAttributes
from datadog_api_client.v2.model.service_update_data import ServiceUpdateData


class TestServiceUpdateData(unittest.TestCase):
    """ServiceUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServiceUpdateData(self):
        """Test ServiceUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServiceUpdateData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
