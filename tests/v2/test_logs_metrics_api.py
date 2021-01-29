# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi  # noqa: E501


class TestLogsMetricsApi(unittest.TestCase):
    """LogsMetricsApi unit test stubs"""

    def setUp(self):
        self.api = LogsMetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_logs_metric(self):
        """Test case for create_logs_metric

        Create a log-based metric  # noqa: E501
        """
        pass

    def test_delete_logs_metric(self):
        """Test case for delete_logs_metric

        Delete a log-based metric  # noqa: E501
        """
        pass

    def test_get_logs_metric(self):
        """Test case for get_logs_metric

        Get a log-based metric  # noqa: E501
        """
        pass

    def test_list_logs_metrics(self):
        """Test case for list_logs_metrics

        Get all log-based metrics  # noqa: E501
        """
        pass

    def test_update_logs_metric(self):
        """Test case for update_logs_metric

        Update a log-based metric  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
