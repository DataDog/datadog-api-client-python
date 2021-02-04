# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_event_aggregation import FormulaAndFunctionEventAggregation
from datadog_api_client.v1.model.formula_and_function_events_sort_type import FormulaAndFunctionEventsSortType
from datadog_api_client.v1.model.query_sort_order import QuerySortOrder

globals()["FormulaAndFunctionEventAggregation"] = FormulaAndFunctionEventAggregation
globals()["FormulaAndFunctionEventsSortType"] = FormulaAndFunctionEventsSortType
globals()["QuerySortOrder"] = QuerySortOrder
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_sort import (
    TimeSeriesFormulaAndFunctionEventQueryDefinitionSort,
)


class TestTimeSeriesFormulaAndFunctionEventQueryDefinitionSort(unittest.TestCase):
    """TimeSeriesFormulaAndFunctionEventQueryDefinitionSort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeSeriesFormulaAndFunctionEventQueryDefinitionSort(self):
        """Test TimeSeriesFormulaAndFunctionEventQueryDefinitionSort"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeSeriesFormulaAndFunctionEventQueryDefinitionSort()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
