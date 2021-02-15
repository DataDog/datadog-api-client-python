# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.api_key import ApiKey

globals()["ApiKey"] = ApiKey
from datadog_api_client.v1.model.api_key_response import ApiKeyResponse


class TestApiKeyResponse(unittest.TestCase):
    """ApiKeyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiKeyResponse(self):
        """Test ApiKeyResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiKeyResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
