# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType
from datadog_api_client.v2.model.metric_tag_configuration_update_attributes import (
    MetricTagConfigurationUpdateAttributes,
)

globals()["MetricTagConfigurationType"] = MetricTagConfigurationType
globals()["MetricTagConfigurationUpdateAttributes"] = MetricTagConfigurationUpdateAttributes
from datadog_api_client.v2.model.metric_tag_configuration_update_data import MetricTagConfigurationUpdateData


class TestMetricTagConfigurationUpdateData(unittest.TestCase):
    """MetricTagConfigurationUpdateData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricTagConfigurationUpdateData(self):
        """Test MetricTagConfigurationUpdateData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricTagConfigurationUpdateData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
