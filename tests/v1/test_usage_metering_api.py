# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi  # noqa: E501


class TestUsageMeteringApi(unittest.TestCase):
    """UsageMeteringApi unit test stubs"""

    def setUp(self):
        self.api = UsageMeteringApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_daily_custom_reports(self):
        """Test case for get_daily_custom_reports

        Get the list of available daily custom reports  # noqa: E501
        """
        pass

    def test_get_incident_management(self):
        """Test case for get_incident_management

        Get hourly usage for incident management  # noqa: E501
        """
        pass

    def test_get_ingested_spans(self):
        """Test case for get_ingested_spans

        Get hourly usage for ingested spans  # noqa: E501
        """
        pass

    def test_get_monthly_custom_reports(self):
        """Test case for get_monthly_custom_reports

        Get the list of available monthly custom reports  # noqa: E501
        """
        pass

    def test_get_specified_daily_custom_reports(self):
        """Test case for get_specified_daily_custom_reports

        Get specified daily custom reports  # noqa: E501
        """
        pass

    def test_get_specified_monthly_custom_reports(self):
        """Test case for get_specified_monthly_custom_reports

        Get specified monthly custom reports  # noqa: E501
        """
        pass

    def test_get_tracing_without_limits(self):
        """Test case for get_tracing_without_limits

        Get hourly usage for tracing without limits  # noqa: E501
        """
        pass

    def test_get_usage_analyzed_logs(self):
        """Test case for get_usage_analyzed_logs

        Get hourly usage for analyzed logs  # noqa: E501
        """
        pass

    def test_get_usage_attribution(self):
        """Test case for get_usage_attribution

        Get Usage Attribution  # noqa: E501
        """
        pass

    def test_get_usage_billable_summary(self):
        """Test case for get_usage_billable_summary

        Get billable usage across your account  # noqa: E501
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

    def test_get_usage_indexed_spans(self):
        """Test case for get_usage_indexed_spans

        Get hourly usage for indexed spans  # noqa: E501
        """
        pass

    def test_get_usage_internet_of_things(self):
        """Test case for get_usage_internet_of_things

        Get hourly usage for IoT  # noqa: E501
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

    def test_get_usage_profiling(self):
        """Test case for get_usage_profiling

        Get hourly usage for profiled hosts  # noqa: E501
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

        Get hourly usage for Synthetics Checks  # noqa: E501
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

        Get top custom metrics by hourly average  # noqa: E501
        """
        pass

    def test_get_usage_trace(self):
        """Test case for get_usage_trace

        Get hourly usage for Trace Search  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
