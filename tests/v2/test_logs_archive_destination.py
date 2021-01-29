# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import logs_archive_destination_azure
except ImportError:
    logs_archive_destination_azure = sys.modules["datadog_api_client.v2.model.logs_archive_destination_azure"]
try:
    from datadog_api_client.v2.model import logs_archive_destination_gcs
except ImportError:
    logs_archive_destination_gcs = sys.modules["datadog_api_client.v2.model.logs_archive_destination_gcs"]
try:
    from datadog_api_client.v2.model import logs_archive_destination_s3
except ImportError:
    logs_archive_destination_s3 = sys.modules["datadog_api_client.v2.model.logs_archive_destination_s3"]
try:
    from datadog_api_client.v2.model import logs_archive_destination_s3_type
except ImportError:
    logs_archive_destination_s3_type = sys.modules["datadog_api_client.v2.model.logs_archive_destination_s3_type"]
try:
    from datadog_api_client.v2.model import logs_archive_integration_s3
except ImportError:
    logs_archive_integration_s3 = sys.modules["datadog_api_client.v2.model.logs_archive_integration_s3"]
from datadog_api_client.v2.model.logs_archive_destination import LogsArchiveDestination


class TestLogsArchiveDestination(unittest.TestCase):
    """LogsArchiveDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsArchiveDestination(self):
        """Test LogsArchiveDestination"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsArchiveDestination()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
