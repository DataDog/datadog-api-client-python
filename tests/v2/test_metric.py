# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metric_type import MetricType

globals()["MetricType"] = MetricType
from datadog_api_client.v2.model.metric import Metric


class TestMetric(unittest.TestCase):
    """Metric unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetric(self):
        """Test Metric"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Metric()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
