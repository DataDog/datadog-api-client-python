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

globals()["FormulaAndFunctionMetricAggregation"] = FormulaAndFunctionMetricAggregation
globals()["FormulaAndFunctionProcessQueryDataSource"] = FormulaAndFunctionProcessQueryDataSource
globals()["QuerySortOrder"] = QuerySortOrder
from datadog_api_client.v1.model.formula_and_function_process_query_definition import (
    FormulaAndFunctionProcessQueryDefinition,
)


class TestFormulaAndFunctionProcessQueryDefinition(unittest.TestCase):
    """FormulaAndFunctionProcessQueryDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFormulaAndFunctionProcessQueryDefinition(self):
        """Test FormulaAndFunctionProcessQueryDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FormulaAndFunctionProcessQueryDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
