# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.api_key import ApiKey
from datadog_api_client.v1.model.application_key import ApplicationKey
from datadog_api_client.v1.model.organization import Organization
from datadog_api_client.v1.model.user import User

globals()["ApiKey"] = ApiKey
globals()["ApplicationKey"] = ApplicationKey
globals()["Organization"] = Organization
globals()["User"] = User
from datadog_api_client.v1.model.organization_create_response import OrganizationCreateResponse


class TestOrganizationCreateResponse(unittest.TestCase):
    """OrganizationCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganizationCreateResponse(self):
        """Test OrganizationCreateResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganizationCreateResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
