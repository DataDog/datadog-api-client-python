# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import synthetics_step
except ImportError:
    synthetics_step = sys.modules["datadog_api_client.v1.model.synthetics_step"]
try:
    from datadog_api_client.v1.model import synthetics_test_config
except ImportError:
    synthetics_test_config = sys.modules["datadog_api_client.v1.model.synthetics_test_config"]
try:
    from datadog_api_client.v1.model import synthetics_test_details_sub_type
except ImportError:
    synthetics_test_details_sub_type = sys.modules["datadog_api_client.v1.model.synthetics_test_details_sub_type"]
try:
    from datadog_api_client.v1.model import synthetics_test_details_type
except ImportError:
    synthetics_test_details_type = sys.modules["datadog_api_client.v1.model.synthetics_test_details_type"]
try:
    from datadog_api_client.v1.model import synthetics_test_options
except ImportError:
    synthetics_test_options = sys.modules["datadog_api_client.v1.model.synthetics_test_options"]
try:
    from datadog_api_client.v1.model import synthetics_test_pause_status
except ImportError:
    synthetics_test_pause_status = sys.modules["datadog_api_client.v1.model.synthetics_test_pause_status"]
from datadog_api_client.v1.model.synthetics_test_details import SyntheticsTestDetails


class TestSyntheticsTestDetails(unittest.TestCase):
    """SyntheticsTestDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsTestDetails(self):
        """Test SyntheticsTestDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsTestDetails()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
