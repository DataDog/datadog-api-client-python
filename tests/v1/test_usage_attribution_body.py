# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_attribution_tag_names import UsageAttributionTagNames
from datadog_api_client.v1.model.usage_attribution_values import UsageAttributionValues

globals()["UsageAttributionTagNames"] = UsageAttributionTagNames
globals()["UsageAttributionValues"] = UsageAttributionValues
from datadog_api_client.v1.model.usage_attribution_body import UsageAttributionBody


class TestUsageAttributionBody(unittest.TestCase):
    """UsageAttributionBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageAttributionBody(self):
        """Test UsageAttributionBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageAttributionBody()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
