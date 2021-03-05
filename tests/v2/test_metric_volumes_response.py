# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.metric_volumes import MetricVolumes

globals()["MetricVolumes"] = MetricVolumes
from datadog_api_client.v2.model.metric_volumes_response import MetricVolumesResponse


class TestMetricVolumesResponse(unittest.TestCase):
    """MetricVolumesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricVolumesResponse(self):
        """Test MetricVolumesResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricVolumesResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
