# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import check_can_delete_monitor_response_data
except ImportError:
    check_can_delete_monitor_response_data = sys.modules[
        "datadog_api_client.v1.model.check_can_delete_monitor_response_data"
    ]
from datadog_api_client.v1.model.check_can_delete_monitor_response import CheckCanDeleteMonitorResponse


class TestCheckCanDeleteMonitorResponse(unittest.TestCase):
    """CheckCanDeleteMonitorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCheckCanDeleteMonitorResponse(self):
        """Test CheckCanDeleteMonitorResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CheckCanDeleteMonitorResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
