# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_filter_create_data import SecurityFilterCreateData

globals()["SecurityFilterCreateData"] = SecurityFilterCreateData
from datadog_api_client.v2.model.security_filter_create_request import SecurityFilterCreateRequest


class TestSecurityFilterCreateRequest(unittest.TestCase):
    """SecurityFilterCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityFilterCreateRequest(self):
        """Test SecurityFilterCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityFilterCreateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
