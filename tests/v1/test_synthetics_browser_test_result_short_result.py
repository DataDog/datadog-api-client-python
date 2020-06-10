# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_device
except ImportError:
    synthetics_device = sys.modules[
        'datadog_api_client.v1.model.synthetics_device']
from datadog_api_client.v1.model.synthetics_browser_test_result_short_result import SyntheticsBrowserTestResultShortResult


class TestSyntheticsBrowserTestResultShortResult(unittest.TestCase):
    """SyntheticsBrowserTestResultShortResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsBrowserTestResultShortResult(self):
        """Test SyntheticsBrowserTestResultShortResult"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsBrowserTestResultShortResult()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
