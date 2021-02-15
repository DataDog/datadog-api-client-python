# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_api_error import LogsAPIError

globals()["LogsAPIError"] = LogsAPIError
from datadog_api_client.v1.model.logs_api_error_response import LogsAPIErrorResponse


class TestLogsAPIErrorResponse(unittest.TestCase):
    """LogsAPIErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsAPIErrorResponse(self):
        """Test LogsAPIErrorResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsAPIErrorResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
