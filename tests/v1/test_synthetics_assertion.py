# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import synthetics_assertion_operator
except ImportError:
    synthetics_assertion_operator = sys.modules[
        'datadog_api_client.v1.model.synthetics_assertion_operator']
try:
    from datadog_api_client.v1.model import synthetics_assertion_type
except ImportError:
    synthetics_assertion_type = sys.modules[
        'datadog_api_client.v1.model.synthetics_assertion_type']
from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion


class TestSyntheticsAssertion(unittest.TestCase):
    """SyntheticsAssertion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAssertion(self):
        """Test SyntheticsAssertion"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAssertion()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
