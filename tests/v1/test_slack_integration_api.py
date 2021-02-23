# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.slack_integration_api import SlackIntegrationApi  # noqa: E501


class TestSlackIntegrationApi(unittest.TestCase):
    """SlackIntegrationApi unit test stubs"""

    def setUp(self):
        self.api = SlackIntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_slack_integration_channel(self):
        """Test case for create_slack_integration_channel

        Create a Slack integration channel  # noqa: E501
        """
        pass

    def test_get_slack_integration_channel(self):
        """Test case for get_slack_integration_channel

        Get a Slack integration channel  # noqa: E501
        """
        pass

    def test_get_slack_integration_channels(self):
        """Test case for get_slack_integration_channels

        Get all channels in a Slack integration  # noqa: E501
        """
        pass

    def test_remove_slack_integration_channel(self):
        """Test case for remove_slack_integration_channel

        Remove a Slack integration channel  # noqa: E501
        """
        pass

    def test_update_slack_integration_channel(self):
        """Test case for update_slack_integration_channel

        Update a Slack integration channel  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
