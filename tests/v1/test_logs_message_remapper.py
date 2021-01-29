# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import logs_message_remapper_type
except ImportError:
    logs_message_remapper_type = sys.modules["datadog_api_client.v1.model.logs_message_remapper_type"]
from datadog_api_client.v1.model.logs_message_remapper import LogsMessageRemapper


class TestLogsMessageRemapper(unittest.TestCase):
    """LogsMessageRemapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsMessageRemapper(self):
        """Test LogsMessageRemapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsMessageRemapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
