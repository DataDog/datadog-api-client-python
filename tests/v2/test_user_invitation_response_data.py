# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import user_invitation_data_attributes
except ImportError:
    user_invitation_data_attributes = sys.modules[
        'datadog_api_client.v2.model.user_invitation_data_attributes']
try:
    from datadog_api_client.v2.model import user_invitations_type
except ImportError:
    user_invitations_type = sys.modules[
        'datadog_api_client.v2.model.user_invitations_type']
from datadog_api_client.v2.model.user_invitation_response_data import UserInvitationResponseData


class TestUserInvitationResponseData(unittest.TestCase):
    """UserInvitationResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserInvitationResponseData(self):
        """Test UserInvitationResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserInvitationResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
