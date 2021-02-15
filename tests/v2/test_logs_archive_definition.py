# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_archive_attributes import LogsArchiveAttributes

globals()["LogsArchiveAttributes"] = LogsArchiveAttributes
from datadog_api_client.v2.model.logs_archive_definition import LogsArchiveDefinition


class TestLogsArchiveDefinition(unittest.TestCase):
    """LogsArchiveDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsArchiveDefinition(self):
        """Test LogsArchiveDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsArchiveDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
