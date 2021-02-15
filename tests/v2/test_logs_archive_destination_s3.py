# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_archive_destination_s3_type import LogsArchiveDestinationS3Type
from datadog_api_client.v2.model.logs_archive_integration_s3 import LogsArchiveIntegrationS3

globals()["LogsArchiveDestinationS3Type"] = LogsArchiveDestinationS3Type
globals()["LogsArchiveIntegrationS3"] = LogsArchiveIntegrationS3
from datadog_api_client.v2.model.logs_archive_destination_s3 import LogsArchiveDestinationS3


class TestLogsArchiveDestinationS3(unittest.TestCase):
    """LogsArchiveDestinationS3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsArchiveDestinationS3(self):
        """Test LogsArchiveDestinationS3"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsArchiveDestinationS3()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
