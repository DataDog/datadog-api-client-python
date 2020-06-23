# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import slo_history_metrics_series
except ImportError:
    slo_history_metrics_series = sys.modules[
        'datadog_api_client.v1.model.slo_history_metrics_series']
from datadog_api_client.v1.model.slo_history_metrics import SLOHistoryMetrics


class TestSLOHistoryMetrics(unittest.TestCase):
    """SLOHistoryMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSLOHistoryMetrics(self):
        """Test SLOHistoryMetrics"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SLOHistoryMetrics()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
