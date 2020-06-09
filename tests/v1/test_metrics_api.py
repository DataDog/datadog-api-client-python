# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.metrics_api import MetricsApi  # noqa: E501


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_metric_metadata(self):
        """Test case for get_metric_metadata

        Get metric metadata  # noqa: E501
        """
        pass

    def test_list_active_metrics(self):
        """Test case for list_active_metrics

        Get active metrics list  # noqa: E501
        """
        pass

    def test_list_metrics(self):
        """Test case for list_metrics

        Search metrics  # noqa: E501
        """
        pass

    def test_query_metrics(self):
        """Test case for query_metrics

        Query timeseries points  # noqa: E501
        """
        pass

    def test_update_metric_metadata(self):
        """Test case for update_metric_metadata

        Edit metric metadata  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
