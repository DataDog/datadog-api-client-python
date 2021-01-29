# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2

try:
    from datadog_api_client.v2.model import organization_attributes
except ImportError:
    organization_attributes = sys.modules["datadog_api_client.v2.model.organization_attributes"]
try:
    from datadog_api_client.v2.model import organizations_type
except ImportError:
    organizations_type = sys.modules["datadog_api_client.v2.model.organizations_type"]
from datadog_api_client.v2.model.organization import Organization


class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganization(self):
        """Test Organization"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Organization()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
