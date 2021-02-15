# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.apm_stats_query_column_type import ApmStatsQueryColumnType
from datadog_api_client.v1.model.apm_stats_query_row_type import ApmStatsQueryRowType

globals()["ApmStatsQueryColumnType"] = ApmStatsQueryColumnType
globals()["ApmStatsQueryRowType"] = ApmStatsQueryRowType
from datadog_api_client.v1.model.apm_stats_query_definition import ApmStatsQueryDefinition


class TestApmStatsQueryDefinition(unittest.TestCase):
    """ApmStatsQueryDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApmStatsQueryDefinition(self):
        """Test ApmStatsQueryDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApmStatsQueryDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
