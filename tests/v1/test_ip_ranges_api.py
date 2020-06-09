# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.ip_ranges_api import IPRangesApi  # noqa: E501


class TestIPRangesApi(unittest.TestCase):
    """IPRangesApi unit test stubs"""

    def setUp(self):
        self.api = IPRangesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ip_ranges(self):
        """Test case for get_ip_ranges

        List IP Ranges  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
