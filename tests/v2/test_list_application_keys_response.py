# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.application_key_response_included_item import ApplicationKeyResponseIncludedItem
from datadog_api_client.v2.model.partial_application_key import PartialApplicationKey

globals()["ApplicationKeyResponseIncludedItem"] = ApplicationKeyResponseIncludedItem
globals()["PartialApplicationKey"] = PartialApplicationKey
from datadog_api_client.v2.model.list_application_keys_response import ListApplicationKeysResponse


class TestListApplicationKeysResponse(unittest.TestCase):
    """ListApplicationKeysResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListApplicationKeysResponse(self):
        """Test ListApplicationKeysResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListApplicationKeysResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
