# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.http_log_item import HTTPLogItem

globals()["HTTPLogItem"] = HTTPLogItem
from datadog_api_client.v1.model.http_log import HTTPLog


class TestHTTPLog(unittest.TestCase):
    """HTTPLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHTTPLog(self):
        """Test HTTPLog"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HTTPLog()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
