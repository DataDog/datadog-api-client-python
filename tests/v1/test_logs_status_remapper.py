# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_status_remapper_type import LogsStatusRemapperType

globals()["LogsStatusRemapperType"] = LogsStatusRemapperType
from datadog_api_client.v1.model.logs_status_remapper import LogsStatusRemapper


class TestLogsStatusRemapper(unittest.TestCase):
    """LogsStatusRemapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsStatusRemapper(self):
        """Test LogsStatusRemapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsStatusRemapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
