# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user_invitation_response_data import UserInvitationResponseData

globals()["UserInvitationResponseData"] = UserInvitationResponseData
from datadog_api_client.v2.model.user_invitations_response import UserInvitationsResponse


class TestUserInvitationsResponse(unittest.TestCase):
    """UserInvitationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserInvitationsResponse(self):
        """Test UserInvitationsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserInvitationsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
