# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_ci_test_metadata_ci
except ImportError:
    synthetics_ci_test_metadata_ci = sys.modules[
        'datadog_api_client.v1.model.synthetics_ci_test_metadata_ci']
try:
    from datadog_api_client.v1.model import synthetics_ci_test_metadata_git
except ImportError:
    synthetics_ci_test_metadata_git = sys.modules[
        'datadog_api_client.v1.model.synthetics_ci_test_metadata_git']
from datadog_api_client.v1.model.synthetics_ci_test_metadata import SyntheticsCITestMetadata


class TestSyntheticsCITestMetadata(unittest.TestCase):
    """SyntheticsCITestMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsCITestMetadata(self):
        """Test SyntheticsCITestMetadata"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsCITestMetadata()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
