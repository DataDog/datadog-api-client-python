# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import organization
except ImportError:
    organization = sys.modules["datadog_api_client.v1.model.organization"]
from datadog_api_client.v1.model.organization_response import OrganizationResponse


class TestOrganizationResponse(unittest.TestCase):
    """OrganizationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganizationResponse(self):
        """Test OrganizationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganizationResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
