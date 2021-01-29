# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_ingested_spans_hour import UsageIngestedSpansHour

globals()["UsageIngestedSpansHour"] = UsageIngestedSpansHour
from datadog_api_client.v1.model.usage_ingested_spans_response import UsageIngestedSpansResponse


class TestUsageIngestedSpansResponse(unittest.TestCase):
    """UsageIngestedSpansResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageIngestedSpansResponse(self):
        """Test UsageIngestedSpansResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageIngestedSpansResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
