# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_filter_exclusion_filter_response import SecurityFilterExclusionFilterResponse
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

globals()["SecurityFilterExclusionFilterResponse"] = SecurityFilterExclusionFilterResponse
globals()["SecurityFilterFilteredDataType"] = SecurityFilterFilteredDataType
from datadog_api_client.v2.model.security_filter_attributes import SecurityFilterAttributes


class TestSecurityFilterAttributes(unittest.TestCase):
    """SecurityFilterAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityFilterAttributes(self):
        """Test SecurityFilterAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityFilterAttributes()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
