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
from datadog_api_client.v1.model.synthetics_parsing_options import SyntheticsParsingOptions


class TestSyntheticsParsingOptions(unittest.TestCase):
    """SyntheticsParsingOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsParsingOptions(self):
        """Test SyntheticsParsingOptions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsParsingOptions()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
