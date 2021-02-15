# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_specified_custom_reports_data import UsageSpecifiedCustomReportsData
from datadog_api_client.v1.model.usage_specified_custom_reports_meta import UsageSpecifiedCustomReportsMeta

globals()["UsageSpecifiedCustomReportsData"] = UsageSpecifiedCustomReportsData
globals()["UsageSpecifiedCustomReportsMeta"] = UsageSpecifiedCustomReportsMeta
from datadog_api_client.v1.model.usage_specified_custom_reports_response import UsageSpecifiedCustomReportsResponse


class TestUsageSpecifiedCustomReportsResponse(unittest.TestCase):
    """UsageSpecifiedCustomReportsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageSpecifiedCustomReportsResponse(self):
        """Test UsageSpecifiedCustomReportsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageSpecifiedCustomReportsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
