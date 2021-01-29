# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import synthetics_device_id
except ImportError:
    synthetics_device_id = sys.modules["datadog_api_client.v1.model.synthetics_device_id"]
try:
    from datadog_api_client.v1.model import synthetics_test_options_retry
except ImportError:
    synthetics_test_options_retry = sys.modules["datadog_api_client.v1.model.synthetics_test_options_retry"]
try:
    from datadog_api_client.v1.model import synthetics_tick_interval
except ImportError:
    synthetics_tick_interval = sys.modules["datadog_api_client.v1.model.synthetics_tick_interval"]
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions


class TestSyntheticsTestOptions(unittest.TestCase):
    """SyntheticsTestOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsTestOptions(self):
        """Test SyntheticsTestOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsTestOptions()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
