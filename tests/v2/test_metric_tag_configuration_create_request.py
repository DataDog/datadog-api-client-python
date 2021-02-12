# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metric_tag_configuration_create_data import MetricTagConfigurationCreateData

globals()["MetricTagConfigurationCreateData"] = MetricTagConfigurationCreateData
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequest


class TestMetricTagConfigurationCreateRequest(unittest.TestCase):
    """MetricTagConfigurationCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricTagConfigurationCreateRequest(self):
        """Test MetricTagConfigurationCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricTagConfigurationCreateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
