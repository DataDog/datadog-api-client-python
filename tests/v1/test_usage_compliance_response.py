# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_compliance_hour import UsageComplianceHour

globals()["UsageComplianceHour"] = UsageComplianceHour
from datadog_api_client.v1.model.usage_compliance_response import UsageComplianceResponse


class TestUsageComplianceResponse(unittest.TestCase):
    """UsageComplianceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageComplianceResponse(self):
        """Test UsageComplianceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageComplianceResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
