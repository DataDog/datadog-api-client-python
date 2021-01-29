# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import usage_specified_custom_reports_data
except ImportError:
    usage_specified_custom_reports_data = sys.modules["datadog_api_client.v1.model.usage_specified_custom_reports_data"]
try:
    from datadog_api_client.v1.model import usage_specified_custom_reports_meta
except ImportError:
    usage_specified_custom_reports_meta = sys.modules["datadog_api_client.v1.model.usage_specified_custom_reports_meta"]
from datadog_api_client.v1.model.usage_specified_custom_reports_response import UsageSpecifiedCustomReportsResponse


class TestUsageSpecifiedCustomReportsResponse(unittest.TestCase):
    """UsageSpecifiedCustomReportsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageSpecifiedCustomReportsResponse(self):
        """Test UsageSpecifiedCustomReportsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageSpecifiedCustomReportsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
