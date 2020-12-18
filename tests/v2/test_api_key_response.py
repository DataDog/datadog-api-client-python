# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.api_key_response_included_item import APIKeyResponseIncludedItem
from datadog_api_client.v2.model.full_api_key import FullAPIKey
globals()['APIKeyResponseIncludedItem'] = APIKeyResponseIncludedItem
globals()['FullAPIKey'] = FullAPIKey
from datadog_api_client.v2.model.api_key_response import APIKeyResponse


class TestAPIKeyResponse(unittest.TestCase):
    """APIKeyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAPIKeyResponse(self):
        """Test APIKeyResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = APIKeyResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
