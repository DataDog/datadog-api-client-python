# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import synthetics_warning_type
except ImportError:
    synthetics_warning_type = sys.modules["datadog_api_client.v1.model.synthetics_warning_type"]
from datadog_api_client.v1.model.synthetics_step_detail_warnings import SyntheticsStepDetailWarnings


class TestSyntheticsStepDetailWarnings(unittest.TestCase):
    """SyntheticsStepDetailWarnings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsStepDetailWarnings(self):
        """Test SyntheticsStepDetailWarnings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsStepDetailWarnings()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
