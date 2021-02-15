# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metric_tag_configuration import MetricTagConfiguration

globals()["MetricTagConfiguration"] = MetricTagConfiguration
from datadog_api_client.v2.model.metric_tag_configuration_response import MetricTagConfigurationResponse


class TestMetricTagConfigurationResponse(unittest.TestCase):
    """MetricTagConfigurationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricTagConfigurationResponse(self):
        """Test MetricTagConfigurationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricTagConfigurationResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
