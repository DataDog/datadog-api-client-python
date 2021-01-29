# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import api_key
except ImportError:
    api_key = sys.modules["datadog_api_client.v1.model.api_key"]
try:
    from datadog_api_client.v1.model import application_key
except ImportError:
    application_key = sys.modules["datadog_api_client.v1.model.application_key"]
try:
    from datadog_api_client.v1.model import organization
except ImportError:
    organization = sys.modules["datadog_api_client.v1.model.organization"]
try:
    from datadog_api_client.v1.model import user
except ImportError:
    user = sys.modules["datadog_api_client.v1.model.user"]
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
