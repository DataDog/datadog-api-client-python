# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody

globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
from datadog_api_client.v1.model.usage_billable_summary_keys import UsageBillableSummaryKeys


class TestUsageBillableSummaryKeys(unittest.TestCase):
    """UsageBillableSummaryKeys unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageBillableSummaryKeys(self):
        """Test UsageBillableSummaryKeys"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageBillableSummaryKeys()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
