# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_api_test_result_data
except ImportError:
    synthetics_api_test_result_data = sys.modules[
        'datadog_api_client.v1.model.synthetics_api_test_result_data']
try:
    from datadog_api_client.v1.model import synthetics_api_test_result_full_check
except ImportError:
    synthetics_api_test_result_full_check = sys.modules[
        'datadog_api_client.v1.model.synthetics_api_test_result_full_check']
try:
    from datadog_api_client.v1.model import synthetics_test_monitor_status
except ImportError:
    synthetics_test_monitor_status = sys.modules[
        'datadog_api_client.v1.model.synthetics_test_monitor_status']
from datadog_api_client.v1.model.synthetics_api_test_result_full import SyntheticsAPITestResultFull


class TestSyntheticsAPITestResultFull(unittest.TestCase):
    """SyntheticsAPITestResultFull unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAPITestResultFull(self):
        """Test SyntheticsAPITestResultFull"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAPITestResultFull()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
