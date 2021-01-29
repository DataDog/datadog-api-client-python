# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_io_t_hour import UsageIoTHour
globals()['UsageIoTHour'] = UsageIoTHour
from datadog_api_client.v1.model.usage_io_t_response import UsageIoTResponse


class TestUsageIoTResponse(unittest.TestCase):
    """UsageIoTResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageIoTResponse(self):
        """Test UsageIoTResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageIoTResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
