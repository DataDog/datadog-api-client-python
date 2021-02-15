# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.gcp_account import GCPAccount

globals()["GCPAccount"] = GCPAccount
from datadog_api_client.v1.model.gcp_account_list_response import GCPAccountListResponse


class TestGCPAccountListResponse(unittest.TestCase):
    """GCPAccountListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGCPAccountListResponse(self):
        """Test GCPAccountListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GCPAccountListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
