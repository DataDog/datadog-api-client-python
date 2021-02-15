# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metrics_and_metric_tag_configurations import MetricsAndMetricTagConfigurations

globals()["MetricsAndMetricTagConfigurations"] = MetricsAndMetricTagConfigurations
from datadog_api_client.v2.model.metrics_and_metric_tag_configurations_response import (
    MetricsAndMetricTagConfigurationsResponse,
)


class TestMetricsAndMetricTagConfigurationsResponse(unittest.TestCase):
    """MetricsAndMetricTagConfigurationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricsAndMetricTagConfigurationsResponse(self):
        """Test MetricsAndMetricTagConfigurationsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricsAndMetricTagConfigurationsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
