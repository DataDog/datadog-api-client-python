# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metric_tag_configuration_create_attributes import (
    MetricTagConfigurationCreateAttributes,
)
from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

globals()["MetricTagConfigurationCreateAttributes"] = MetricTagConfigurationCreateAttributes
globals()["MetricTagConfigurationType"] = MetricTagConfigurationType
from datadog_api_client.v2.model.metric_tag_configuration_create_data import MetricTagConfigurationCreateData


class TestMetricTagConfigurationCreateData(unittest.TestCase):
    """MetricTagConfigurationCreateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricTagConfigurationCreateData(self):
        """Test MetricTagConfigurationCreateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricTagConfigurationCreateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
