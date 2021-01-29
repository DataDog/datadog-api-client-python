# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.hosts_api import HostsApi  # noqa: E501


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self):
        self.api = HostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_host_totals(self):
        """Test case for get_host_totals

        Get the total number of active hosts  # noqa: E501
        """
        pass

    def test_list_hosts(self):
        """Test case for list_hosts

        Get all hosts for your organization  # noqa: E501
        """
        pass

    def test_mute_host(self):
        """Test case for mute_host

        Mute a host  # noqa: E501
        """
        pass

    def test_unmute_host(self):
        """Test case for unmute_host

        Unmute a host  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
