# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_browser_error_type
except ImportError:
    synthetics_browser_error_type = sys.modules[
        'datadog_api_client.v1.model.synthetics_browser_error_type']
from datadog_api_client.v1.model.synthetics_browser_error import SyntheticsBrowserError


class TestSyntheticsBrowserError(unittest.TestCase):
    """SyntheticsBrowserError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsBrowserError(self):
        """Test SyntheticsBrowserError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsBrowserError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
