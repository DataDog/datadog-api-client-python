# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_events_data_source import FormulaAndFunctionEventsDataSource
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_compute import TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_group_by import TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_search import TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch
globals()['FormulaAndFunctionEventsDataSource'] = FormulaAndFunctionEventsDataSource
globals()['TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute'] = TimeSeriesFormulaAndFunctionEventQueryDefinitionCompute
globals()['TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy'] = TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy
globals()['TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch'] = TimeSeriesFormulaAndFunctionEventQueryDefinitionSearch
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition import TimeSeriesFormulaAndFunctionEventQueryDefinition


class TestTimeSeriesFormulaAndFunctionEventQueryDefinition(unittest.TestCase):
    """TimeSeriesFormulaAndFunctionEventQueryDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeSeriesFormulaAndFunctionEventQueryDefinition(self):
        """Test TimeSeriesFormulaAndFunctionEventQueryDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeSeriesFormulaAndFunctionEventQueryDefinition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
