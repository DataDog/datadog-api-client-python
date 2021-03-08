# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options_type import (
    SyntheticsGlobalVariableParseTestOptionsType,
)
from datadog_api_client.v1.model.synthetics_variable_parser import SyntheticsVariableParser

globals()["SyntheticsGlobalVariableParseTestOptionsType"] = SyntheticsGlobalVariableParseTestOptionsType
globals()["SyntheticsVariableParser"] = SyntheticsVariableParser
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options import (
    SyntheticsGlobalVariableParseTestOptions,
)


class TestSyntheticsGlobalVariableParseTestOptions(unittest.TestCase):
    """SyntheticsGlobalVariableParseTestOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsGlobalVariableParseTestOptions(self):
        """Test SyntheticsGlobalVariableParseTestOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsGlobalVariableParseTestOptions()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
