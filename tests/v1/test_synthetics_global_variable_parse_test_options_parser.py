# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_global_variable_parser_type import SyntheticsGlobalVariableParserType
globals()['SyntheticsGlobalVariableParserType'] = SyntheticsGlobalVariableParserType
from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options_parser import SyntheticsGlobalVariableParseTestOptionsParser


class TestSyntheticsGlobalVariableParseTestOptionsParser(unittest.TestCase):
    """SyntheticsGlobalVariableParseTestOptionsParser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsGlobalVariableParseTestOptionsParser(self):
        """Test SyntheticsGlobalVariableParseTestOptionsParser"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsGlobalVariableParseTestOptionsParser()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
