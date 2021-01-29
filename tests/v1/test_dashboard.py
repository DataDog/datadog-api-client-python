# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import dashboard_layout_type
except ImportError:
    dashboard_layout_type = sys.modules["datadog_api_client.v1.model.dashboard_layout_type"]
try:
    from datadog_api_client.v1.model import dashboard_template_variable_preset
except ImportError:
    dashboard_template_variable_preset = sys.modules["datadog_api_client.v1.model.dashboard_template_variable_preset"]
try:
    from datadog_api_client.v1.model import dashboard_template_variables
except ImportError:
    dashboard_template_variables = sys.modules["datadog_api_client.v1.model.dashboard_template_variables"]
try:
    from datadog_api_client.v1.model import widget
except ImportError:
    widget = sys.modules["datadog_api_client.v1.model.widget"]
from datadog_api_client.v1.model.dashboard import Dashboard


class TestDashboard(unittest.TestCase):
    """Dashboard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboard(self):
        """Test Dashboard"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Dashboard()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
