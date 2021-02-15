# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_attribution_body import UsageAttributionBody
from datadog_api_client.v1.model.usage_attribution_metadata import UsageAttributionMetadata

globals()["UsageAttributionBody"] = UsageAttributionBody
globals()["UsageAttributionMetadata"] = UsageAttributionMetadata
from datadog_api_client.v1.model.usage_attribution_response import UsageAttributionResponse


class TestUsageAttributionResponse(unittest.TestCase):
    """UsageAttributionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageAttributionResponse(self):
        """Test UsageAttributionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageAttributionResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
