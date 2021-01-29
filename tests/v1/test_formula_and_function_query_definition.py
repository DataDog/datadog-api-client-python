# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_process_query_data_source import (
    FormulaAndFunctionProcessQueryDataSource,
)
from datadog_api_client.v1.model.query_sort_order import QuerySortOrder
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition import (
    TimeSeriesFormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_compute import (
    TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute,
)
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_group_by import (
    TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy,
)
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_search import (
    TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch,
)
from datadog_api_client.v1.model.time_series_formula_and_function_metric_query_definition import (
    TimeSeriesFormulaAndFunctionMetricQueryDefinition,
)
from datadog_api_client.v1.model.time_series_formula_and_function_process_query_definition import (
    TimeSeriesFormulaAndFunctionProcessQueryDefinition,
)

globals()["FormulaAndFunctionMetricAggregation"] = FormulaAndFunctionMetricAggregation
globals()["FormulaAndFunctionProcessQueryDataSource"] = FormulaAndFunctionProcessQueryDataSource
globals()["QuerySortOrder"] = QuerySortOrder
globals()["TimeSeriesFormulaAndFunctionEventQueryDefinition"] = TimeSeriesFormulaAndFunctionEventQueryDefinition
globals()[
    "TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute"
] = TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute
globals()[
    "TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy"
] = TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy
globals()[
    "TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch"
] = TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch
globals()["TimeSeriesFormulaAndFunctionMetricQueryDefinition"] = TimeSeriesFormulaAndFunctionMetricQueryDefinition
globals()["TimeSeriesFormulaAndFunctionProcessQueryDefinition"] = TimeSeriesFormulaAndFunctionProcessQueryDefinition
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
