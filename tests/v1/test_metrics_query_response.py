# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.metrics_query_metadata import MetricsQueryMetadata

globals()["MetricsQueryMetadata"] = MetricsQueryMetadata
from datadog_api_client.v1.model.metrics_query_response import MetricsQueryResponse


class TestMetricsQueryResponse(unittest.TestCase):
    """MetricsQueryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricsQueryResponse(self):
        """Test MetricsQueryResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricsQueryResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
