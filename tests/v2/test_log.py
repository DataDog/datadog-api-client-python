# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.log_attributes import LogAttributes
from datadog_api_client.v2.model.log_type import LogType

globals()["LogAttributes"] = LogAttributes
globals()["LogType"] = LogType
from datadog_api_client.v2.model.log import Log


class TestLog(unittest.TestCase):
    """Log unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLog(self):
        """Test Log"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Log()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
