# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_index import LogsIndex

globals()["LogsIndex"] = LogsIndex
from datadog_api_client.v1.model.logs_index_list_response import LogsIndexListResponse


class TestLogsIndexListResponse(unittest.TestCase):
    """LogsIndexListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsIndexListResponse(self):
        """Test LogsIndexListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsIndexListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
