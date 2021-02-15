# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_network_flows_hour import UsageNetworkFlowsHour

globals()["UsageNetworkFlowsHour"] = UsageNetworkFlowsHour
from datadog_api_client.v1.model.usage_network_flows_response import UsageNetworkFlowsResponse


class TestUsageNetworkFlowsResponse(unittest.TestCase):
    """UsageNetworkFlowsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageNetworkFlowsResponse(self):
        """Test UsageNetworkFlowsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageNetworkFlowsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
