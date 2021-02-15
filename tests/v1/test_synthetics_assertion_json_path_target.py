# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_assertion_json_path_operator import SyntheticsAssertionJSONPathOperator
from datadog_api_client.v1.model.synthetics_assertion_json_path_target_target import (
    SyntheticsAssertionJSONPathTargetTarget,
)
from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType

globals()["SyntheticsAssertionJSONPathOperator"] = SyntheticsAssertionJSONPathOperator
globals()["SyntheticsAssertionJSONPathTargetTarget"] = SyntheticsAssertionJSONPathTargetTarget
globals()["SyntheticsAssertionType"] = SyntheticsAssertionType
from datadog_api_client.v1.model.synthetics_assertion_json_path_target import SyntheticsAssertionJSONPathTarget


class TestSyntheticsAssertionJSONPathTarget(unittest.TestCase):
    """SyntheticsAssertionJSONPathTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsAssertionJSONPathTarget(self):
        """Test SyntheticsAssertionJSONPathTarget"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsAssertionJSONPathTarget()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
