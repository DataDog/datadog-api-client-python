# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType

globals()["SyntheticsAssertionOperator"] = SyntheticsAssertionOperator
globals()["SyntheticsAssertionType"] = SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget


class TestSyntheticsAssertionTarget(unittest.TestCase):
    """SyntheticsAssertionTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAssertionTarget(self):
        """Test SyntheticsAssertionTarget"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAssertionTarget()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
