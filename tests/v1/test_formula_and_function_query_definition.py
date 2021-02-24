# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_event_query_definition import (
    FormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_event_query_definition_compute import (
    FormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.formula_and_function_event_query_definition_search import (
    FormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.formula_and_function_event_query_group_by import FormulaAndFunctionEventQueryGroupBy
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_process_query_data_source import (
    FormulaAndFunctionProcessQueryDataSource,
)
from datadog_api_client.v1.model.formula_and_function_process_query_definition import (
    FormulaAndFunctionProcessQueryDefinition,
)
from datadog_api_client.v1.model.query_sort_order import QuerySortOrder

globals()["FormulaAndFunctionEventQueryDefinition"] = FormulaAndFunctionEventQueryDefinition
globals()["FormulaAndFunctionEventQueryDefinitionCompute"] = FormulaAndFunctionEventQueryDefinitionCompute
globals()["FormulaAndFunctionEventQueryDefinitionSearch"] = FormulaAndFunctionEventQueryDefinitionSearch
globals()["FormulaAndFunctionEventQueryGroupBy"] = FormulaAndFunctionEventQueryGroupBy
globals()["FormulaAndFunctionMetricAggregation"] = FormulaAndFunctionMetricAggregation
globals()["FormulaAndFunctionMetricQueryDefinition"] = FormulaAndFunctionMetricQueryDefinition
globals()["FormulaAndFunctionProcessQueryDataSource"] = FormulaAndFunctionProcessQueryDataSource
globals()["FormulaAndFunctionProcessQueryDefinition"] = FormulaAndFunctionProcessQueryDefinition
globals()["QuerySortOrder"] = QuerySortOrder
from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition


class TestFormulaAndFunctionQueryDefinition(unittest.TestCase):
    """FormulaAndFunctionQueryDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFormulaAndFunctionQueryDefinition(self):
        """Test FormulaAndFunctionQueryDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FormulaAndFunctionQueryDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
