# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.api_key_update_attributes import APIKeyUpdateAttributes
from datadog_api_client.v2.model.api_keys_type import APIKeysType

globals()["APIKeyUpdateAttributes"] = APIKeyUpdateAttributes
globals()["APIKeysType"] = APIKeysType
from datadog_api_client.v2.model.api_key_update_data import APIKeyUpdateData


class TestAPIKeyUpdateData(unittest.TestCase):
    """APIKeyUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAPIKeyUpdateData(self):
        """Test APIKeyUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = APIKeyUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
