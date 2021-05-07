# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_filter import SecurityFilter
from datadog_api_client.v2.model.security_filter_meta import SecurityFilterMeta

globals()["SecurityFilter"] = SecurityFilter
globals()["SecurityFilterMeta"] = SecurityFilterMeta
from datadog_api_client.v2.model.security_filter_response import SecurityFilterResponse


class TestSecurityFilterResponse(unittest.TestCase):
    """SecurityFilterResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityFilterResponse(self):
        """Test SecurityFilterResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityFilterResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
