# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_summary_date_org import UsageSummaryDateOrg

globals()["UsageSummaryDateOrg"] = UsageSummaryDateOrg
from datadog_api_client.v1.model.usage_summary_date import UsageSummaryDate


class TestUsageSummaryDate(unittest.TestCase):
    """UsageSummaryDate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageSummaryDate(self):
        """Test UsageSummaryDate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageSummaryDate()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
