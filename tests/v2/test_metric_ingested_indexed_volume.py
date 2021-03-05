# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metric_ingested_indexed_volume_attributes import MetricIngestedIndexedVolumeAttributes
from datadog_api_client.v2.model.metric_ingested_indexed_volume_type import MetricIngestedIndexedVolumeType

globals()["MetricIngestedIndexedVolumeAttributes"] = MetricIngestedIndexedVolumeAttributes
globals()["MetricIngestedIndexedVolumeType"] = MetricIngestedIndexedVolumeType
from datadog_api_client.v2.model.metric_ingested_indexed_volume import MetricIngestedIndexedVolume


class TestMetricIngestedIndexedVolume(unittest.TestCase):
    """MetricIngestedIndexedVolume unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricIngestedIndexedVolume(self):
        """Test MetricIngestedIndexedVolume"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricIngestedIndexedVolume()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
