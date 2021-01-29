# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_exclusion import LogsExclusion
from datadog_api_client.v1.model.logs_filter import LogsFilter

globals()["LogsExclusion"] = LogsExclusion
globals()["LogsFilter"] = LogsFilter
from datadog_api_client.v1.model.logs_index_update_request import LogsIndexUpdateRequest


class TestLogsIndexUpdateRequest(unittest.TestCase):
    """LogsIndexUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsIndexUpdateRequest(self):
        """Test LogsIndexUpdateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsIndexUpdateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
