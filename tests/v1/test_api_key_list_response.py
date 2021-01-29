# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import api_key
except ImportError:
    api_key = sys.modules["datadog_api_client.v1.model.api_key"]
from datadog_api_client.v1.model.api_key_list_response import ApiKeyListResponse


class TestApiKeyListResponse(unittest.TestCase):
    """ApiKeyListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiKeyListResponse(self):
        """Test ApiKeyListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiKeyListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
