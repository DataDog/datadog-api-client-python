# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_event_query_definition_compute import (
    FormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.formula_and_function_event_query_definition_search import (
    FormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.formula_and_function_event_query_group_by import FormulaAndFunctionEventQueryGroupBy
from datadog_api_client.v1.model.formula_and_function_events_data_source import FormulaAndFunctionEventsDataSource

globals()["FormulaAndFunctionEventQueryDefinitionCompute"] = FormulaAndFunctionEventQueryDefinitionCompute
globals()["FormulaAndFunctionEventQueryDefinitionSearch"] = FormulaAndFunctionEventQueryDefinitionSearch
globals()["FormulaAndFunctionEventQueryGroupBy"] = FormulaAndFunctionEventQueryGroupBy
globals()["FormulaAndFunctionEventsDataSource"] = FormulaAndFunctionEventsDataSource
from datadog_api_client.v1.model.formula_and_function_event_query_definition import (
    FormulaAndFunctionEventQueryDefinition,
)


class TestFormulaAndFunctionEventQueryDefinition(unittest.TestCase):
    """FormulaAndFunctionEventQueryDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFormulaAndFunctionEventQueryDefinition(self):
        """Test FormulaAndFunctionEventQueryDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FormulaAndFunctionEventQueryDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
