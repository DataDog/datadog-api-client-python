# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.role_update_response_data import RoleUpdateResponseData

globals()["RoleUpdateResponseData"] = RoleUpdateResponseData
from datadog_api_client.v2.model.role_update_response import RoleUpdateResponse


class TestRoleUpdateResponse(unittest.TestCase):
    """RoleUpdateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoleUpdateResponse(self):
        """Test RoleUpdateResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoleUpdateResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
