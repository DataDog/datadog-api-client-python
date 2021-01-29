# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import usage_profiling_hour
except ImportError:
    usage_profiling_hour = sys.modules["datadog_api_client.v1.model.usage_profiling_hour"]
from datadog_api_client.v1.model.usage_profiling_response import UsageProfilingResponse


class TestUsageProfilingResponse(unittest.TestCase):
    """UsageProfilingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageProfilingResponse(self):
        """Test UsageProfilingResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageProfilingResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
