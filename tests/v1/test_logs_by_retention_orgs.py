# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_by_retention_org_usage import LogsByRetentionOrgUsage

globals()["LogsByRetentionOrgUsage"] = LogsByRetentionOrgUsage
from datadog_api_client.v1.model.logs_by_retention_orgs import LogsByRetentionOrgs


class TestLogsByRetentionOrgs(unittest.TestCase):
    """LogsByRetentionOrgs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsByRetentionOrgs(self):
        """Test LogsByRetentionOrgs"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsByRetentionOrgs()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
