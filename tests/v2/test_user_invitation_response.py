# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user_invitation_response_data import UserInvitationResponseData

globals()["UserInvitationResponseData"] = UserInvitationResponseData
from datadog_api_client.v2.model.user_invitation_response import UserInvitationResponse


class TestUserInvitationResponse(unittest.TestCase):
    """UserInvitationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserInvitationResponse(self):
        """Test UserInvitationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserInvitationResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
