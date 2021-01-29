# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi  # noqa: E501


class TestUsageMeteringApi(unittest.TestCase):
    """UsageMeteringApi unit test stubs"""

    def setUp(self):
        self.api = UsageMeteringApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_usage_analyzed_logs(self):
        """Test case for get_usage_analyzed_logs

        Get hourly usage for analyzed logs  # noqa: E501
        """
        pass

    def test_get_usage_fargate(self):
        """Test case for get_usage_fargate

        Get hourly usage for Fargate  # noqa: E501
        """
        pass

    def test_get_usage_hosts(self):
        """Test case for get_usage_hosts

        Get hourly usage for hosts and containers  # noqa: E501
        """
        pass

    def test_get_usage_lambda(self):
        """Test case for get_usage_lambda

        Get hourly usage for Lambda  # noqa: E501
        """
        pass

    def test_get_usage_logs(self):
        """Test case for get_usage_logs

        Get hourly usage for Logs  # noqa: E501
        """
        pass

    def test_get_usage_logs_by_index(self):
        """Test case for get_usage_logs_by_index

        Get hourly usage for Logs by Index  # noqa: E501
        """
        pass

    def test_get_usage_network_flows(self):
        """Test case for get_usage_network_flows

        Get hourly usage for Network Flows  # noqa: E501
        """
        pass

    def test_get_usage_network_hosts(self):
        """Test case for get_usage_network_hosts

        Get hourly usage for Network Hosts  # noqa: E501
        """
        pass

    def test_get_usage_rum_sessions(self):
        """Test case for get_usage_rum_sessions

        Get hourly usage for RUM Sessions  # noqa: E501
        """
        pass

    def test_get_usage_snmp(self):
        """Test case for get_usage_snmp

        Get hourly usage for SNMP devices  # noqa: E501
        """
        pass

    def test_get_usage_summary(self):
        """Test case for get_usage_summary

        Get usage across your multi-org account  # noqa: E501
        """
        pass

    def test_get_usage_synthetics(self):
        """Test case for get_usage_synthetics

        Get hourly usage for Synthetics API Checks  # noqa: E501
        """
        pass

    def test_get_usage_synthetics_api(self):
        """Test case for get_usage_synthetics_api

        Get hourly usage for Synthetics API Checks  # noqa: E501
        """
        pass

    def test_get_usage_synthetics_browser(self):
        """Test case for get_usage_synthetics_browser

        Get hourly usage for Synthetics Browser Checks  # noqa: E501
        """
        pass

    def test_get_usage_timeseries(self):
        """Test case for get_usage_timeseries

        Get hourly usage for custom metrics  # noqa: E501
        """
        pass

    def test_get_usage_top_avg_metrics(self):
        """Test case for get_usage_top_avg_metrics

        Get top 500 custom metrics by hourly average  # noqa: E501
        """
        pass

    def test_get_usage_trace(self):
        """Test case for get_usage_trace

        Get hourly usage for Trace Search  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
