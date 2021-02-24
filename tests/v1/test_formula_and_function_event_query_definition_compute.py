# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_event_aggregation import FormulaAndFunctionEventAggregation

globals()["FormulaAndFunctionEventAggregation"] = FormulaAndFunctionEventAggregation
from datadog_api_client.v1.model.formula_and_function_event_query_definition_compute import (
    FormulaAndFunctionEventQueryDefinitionCompute,
)


class TestFormulaAndFunctionEventQueryDefinitionCompute(unittest.TestCase):
    """FormulaAndFunctionEventQueryDefinitionCompute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFormulaAndFunctionEventQueryDefinitionCompute(self):
        """Test FormulaAndFunctionEventQueryDefinitionCompute"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FormulaAndFunctionEventQueryDefinitionCompute()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
