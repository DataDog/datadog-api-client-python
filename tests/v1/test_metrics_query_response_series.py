# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import metrics_query_response_unit
except ImportError:
    metrics_query_response_unit = sys.modules[
        'datadog_api_client.v1.model.metrics_query_response_unit']
try:
    from datadog_api_client.v1.model import point
except ImportError:
    point = sys.modules[
        'datadog_api_client.v1.model.point']
from datadog_api_client.v1.model.metrics_query_response_series import MetricsQueryResponseSeries


class TestMetricsQueryResponseSeries(unittest.TestCase):
    """MetricsQueryResponseSeries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricsQueryResponseSeries(self):
        """Test MetricsQueryResponseSeries"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricsQueryResponseSeries()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
