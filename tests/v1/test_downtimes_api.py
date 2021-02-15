# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.downtimes_api import DowntimesApi  # noqa: E501


class TestDowntimesApi(unittest.TestCase):
    """DowntimesApi unit test stubs"""

    def setUp(self):
        self.api = DowntimesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_downtime(self):
        """Test case for cancel_downtime

        Cancel a downtime  # noqa: E501
        """
        pass

    def test_cancel_downtimes_by_scope(self):
        """Test case for cancel_downtimes_by_scope

        Cancel downtimes by scope  # noqa: E501
        """
        pass

    def test_create_downtime(self):
        """Test case for create_downtime

        Schedule a downtime  # noqa: E501
        """
        pass

    def test_get_downtime(self):
        """Test case for get_downtime

        Get a downtime  # noqa: E501
        """
        pass

    def test_list_downtimes(self):
        """Test case for list_downtimes

        Get all downtimes  # noqa: E501
        """
        pass

    def test_update_downtime(self):
        """Test case for update_downtime

        Update a downtime  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
