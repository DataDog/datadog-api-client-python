# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import synthetics_basic_auth
except ImportError:
    synthetics_basic_auth = sys.modules["datadog_api_client.v1.model.synthetics_basic_auth"]
try:
    from datadog_api_client.v1.model import synthetics_ci_test_metadata
except ImportError:
    synthetics_ci_test_metadata = sys.modules["datadog_api_client.v1.model.synthetics_ci_test_metadata"]
try:
    from datadog_api_client.v1.model import synthetics_device_id
except ImportError:
    synthetics_device_id = sys.modules["datadog_api_client.v1.model.synthetics_device_id"]
try:
    from datadog_api_client.v1.model import synthetics_test_headers
except ImportError:
    synthetics_test_headers = sys.modules["datadog_api_client.v1.model.synthetics_test_headers"]
try:
    from datadog_api_client.v1.model import synthetics_test_options_retry
except ImportError:
    synthetics_test_options_retry = sys.modules["datadog_api_client.v1.model.synthetics_test_options_retry"]
from datadog_api_client.v1.model.synthetics_ci_test import SyntheticsCITest


class TestSyntheticsCITest(unittest.TestCase):
    """SyntheticsCITest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsCITest(self):
        """Test SyntheticsCITest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsCITest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
