# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.log_query_definition_group_by_sort import LogQueryDefinitionGroupBySort

globals()["LogQueryDefinitionGroupBySort"] = LogQueryDefinitionGroupBySort
from datadog_api_client.v1.model.log_query_definition_group_by import LogQueryDefinitionGroupBy


class TestLogQueryDefinitionGroupBy(unittest.TestCase):
    """LogQueryDefinitionGroupBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogQueryDefinitionGroupBy(self):
        """Test LogQueryDefinitionGroupBy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogQueryDefinitionGroupBy()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
