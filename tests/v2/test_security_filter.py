# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_filter_attributes import SecurityFilterAttributes
from datadog_api_client.v2.model.security_filter_type import SecurityFilterType

globals()["SecurityFilterAttributes"] = SecurityFilterAttributes
globals()["SecurityFilterType"] = SecurityFilterType
from datadog_api_client.v2.model.security_filter import SecurityFilter


class TestSecurityFilter(unittest.TestCase):
    """SecurityFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityFilter(self):
        """Test SecurityFilter"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityFilter()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
