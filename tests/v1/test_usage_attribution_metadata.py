# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_attribution_aggregates import UsageAttributionAggregates
from datadog_api_client.v1.model.usage_attribution_pagination import UsageAttributionPagination

globals()["UsageAttributionAggregates"] = UsageAttributionAggregates
globals()["UsageAttributionPagination"] = UsageAttributionPagination
from datadog_api_client.v1.model.usage_attribution_metadata import UsageAttributionMetadata


class TestUsageAttributionMetadata(unittest.TestCase):
    """UsageAttributionMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageAttributionMetadata(self):
        """Test UsageAttributionMetadata"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageAttributionMetadata()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
