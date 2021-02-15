# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_group_by_sort import (
    TimeSeriesFormulaAndFunctionEventQueryGroupBySort,
)

globals()["TimeSeriesFormulaAndFunctionEventQueryGroupBySort"] = TimeSeriesFormulaAndFunctionEventQueryGroupBySort
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_group_by import (
    TimeSeriesFormulaAndFunctionEventQueryGroupBy,
)


class TestTimeSeriesFormulaAndFunctionEventQueryGroupBy(unittest.TestCase):
    """TimeSeriesFormulaAndFunctionEventQueryGroupBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeSeriesFormulaAndFunctionEventQueryGroupBy(self):
        """Test TimeSeriesFormulaAndFunctionEventQueryGroupBy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeSeriesFormulaAndFunctionEventQueryGroupBy()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
