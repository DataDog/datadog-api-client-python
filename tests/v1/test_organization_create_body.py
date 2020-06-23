# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import organization_billing
except ImportError:
    organization_billing = sys.modules[
        'datadog_api_client.v1.model.organization_billing']
try:
    from datadog_api_client.v1.model import organization_subscription
except ImportError:
    organization_subscription = sys.modules[
        'datadog_api_client.v1.model.organization_subscription']
from datadog_api_client.v1.model.organization_create_body import OrganizationCreateBody


class TestOrganizationCreateBody(unittest.TestCase):
    """OrganizationCreateBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganizationCreateBody(self):
        """Test OrganizationCreateBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganizationCreateBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
