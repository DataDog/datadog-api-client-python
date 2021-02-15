# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi  # noqa: E501


class TestLogsPipelinesApi(unittest.TestCase):
    """LogsPipelinesApi unit test stubs"""

    def setUp(self):
        self.api = LogsPipelinesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_logs_pipeline(self):
        """Test case for create_logs_pipeline

        Create a pipeline  # noqa: E501
        """
        pass

    def test_delete_logs_pipeline(self):
        """Test case for delete_logs_pipeline

        Delete a pipeline  # noqa: E501
        """
        pass

    def test_get_logs_pipeline(self):
        """Test case for get_logs_pipeline

        Get a pipeline  # noqa: E501
        """
        pass

    def test_get_logs_pipeline_order(self):
        """Test case for get_logs_pipeline_order

        Get pipeline order  # noqa: E501
        """
        pass

    def test_list_logs_pipelines(self):
        """Test case for list_logs_pipelines

        Get all pipelines  # noqa: E501
        """
        pass

    def test_update_logs_pipeline(self):
        """Test case for update_logs_pipeline

        Update a pipeline  # noqa: E501
        """
        pass

    def test_update_logs_pipeline_order(self):
        """Test case for update_logs_pipeline_order

        Update pipeline order  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
