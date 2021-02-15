# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

globals()["ApplicationKeyCreateAttributes"] = ApplicationKeyCreateAttributes
globals()["ApplicationKeysType"] = ApplicationKeysType
from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData


class TestApplicationKeyCreateData(unittest.TestCase):
    """ApplicationKeyCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationKeyCreateData(self):
        """Test ApplicationKeyCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationKeyCreateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
