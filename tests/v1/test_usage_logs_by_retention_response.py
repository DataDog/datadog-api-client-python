# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_logs_by_retention_hour import UsageLogsByRetentionHour

globals()["UsageLogsByRetentionHour"] = UsageLogsByRetentionHour
from datadog_api_client.v1.model.usage_logs_by_retention_response import UsageLogsByRetentionResponse


class TestUsageLogsByRetentionResponse(unittest.TestCase):
    """UsageLogsByRetentionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageLogsByRetentionResponse(self):
        """Test UsageLogsByRetentionResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageLogsByRetentionResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
