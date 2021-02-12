# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v2
from datadog_api_client.v2.api.metrics_api import MetricsApi  # noqa: E501


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tag_configuration(self):
        """Test case for create_tag_configuration

        Create a Tag Configuration  # noqa: E501
        """
        pass

    def test_delete_tag_configuration(self):
        """Test case for delete_tag_configuration

        Delete a Tag Configuration  # noqa: E501
        """
        pass

    def test_list_tag_configuration_by_name(self):
        """Test case for list_tag_configuration_by_name

        List Tag Configuration by Name  # noqa: E501
        """
        pass

    def test_list_tag_configurations(self):
        """Test case for list_tag_configurations

        List Tag Configurations  # noqa: E501
        """
        pass

    def test_update_tag_configuration(self):
        """Test case for update_tag_configuration

        Update a Tag Configuration  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
