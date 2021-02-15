# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_archive_create_request_definition import LogsArchiveCreateRequestDefinition

globals()["LogsArchiveCreateRequestDefinition"] = LogsArchiveCreateRequestDefinition
from datadog_api_client.v2.model.logs_archive_create_request import LogsArchiveCreateRequest


class TestLogsArchiveCreateRequest(unittest.TestCase):
    """LogsArchiveCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsArchiveCreateRequest(self):
        """Test LogsArchiveCreateRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsArchiveCreateRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
