# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.api_key_relationships import APIKeyRelationships
from datadog_api_client.v2.model.api_keys_type import APIKeysType
from datadog_api_client.v2.model.full_api_key_attributes import FullAPIKeyAttributes

globals()["APIKeyRelationships"] = APIKeyRelationships
globals()["APIKeysType"] = APIKeysType
globals()["FullAPIKeyAttributes"] = FullAPIKeyAttributes
from datadog_api_client.v2.model.full_api_key import FullAPIKey


class TestFullAPIKey(unittest.TestCase):
    """FullAPIKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFullAPIKey(self):
        """Test FullAPIKey"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FullAPIKey()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
