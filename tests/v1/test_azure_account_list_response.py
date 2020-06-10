# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import azure_account
except ImportError:
    azure_account = sys.modules[
        'datadog_api_client.v1.model.azure_account']
from datadog_api_client.v1.model.azure_account_list_response import AzureAccountListResponse


class TestAzureAccountListResponse(unittest.TestCase):
    """AzureAccountListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAzureAccountListResponse(self):
        """Test AzureAccountListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AzureAccountListResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
