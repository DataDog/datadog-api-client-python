# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.user_invitation_relationships import UserInvitationRelationships
from datadog_api_client.v2.model.user_invitations_type import UserInvitationsType

globals()["UserInvitationRelationships"] = UserInvitationRelationships
globals()["UserInvitationsType"] = UserInvitationsType
from datadog_api_client.v2.model.user_invitation_data import UserInvitationData


class TestUserInvitationData(unittest.TestCase):
    """UserInvitationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserInvitationData(self):
        """Test UserInvitationData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserInvitationData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
