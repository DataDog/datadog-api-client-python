# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import creator
except ImportError:
    creator = sys.modules["datadog_api_client.v1.model.creator"]
from datadog_api_client.v1.model.dashboard_list import DashboardList


class TestDashboardList(unittest.TestCase):
    """DashboardList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardList(self):
        """Test DashboardList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardList()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
