# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_user_agent_parser_type import LogsUserAgentParserType

globals()["LogsUserAgentParserType"] = LogsUserAgentParserType
from datadog_api_client.v1.model.logs_user_agent_parser import LogsUserAgentParser


class TestLogsUserAgentParser(unittest.TestCase):
    """LogsUserAgentParser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsUserAgentParser(self):
        """Test LogsUserAgentParser"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsUserAgentParser()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
