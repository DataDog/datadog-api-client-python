# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_archive_order_attributes import LogsArchiveOrderAttributes
from datadog_api_client.v2.model.logs_archive_order_definition_type import LogsArchiveOrderDefinitionType

globals()["LogsArchiveOrderAttributes"] = LogsArchiveOrderAttributes
globals()["LogsArchiveOrderDefinitionType"] = LogsArchiveOrderDefinitionType
from datadog_api_client.v2.model.logs_archive_order_definition import LogsArchiveOrderDefinition


class TestLogsArchiveOrderDefinition(unittest.TestCase):
    """LogsArchiveOrderDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsArchiveOrderDefinition(self):
        """Test LogsArchiveOrderDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsArchiveOrderDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
