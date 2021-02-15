# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.organization_attributes import OrganizationAttributes
from datadog_api_client.v2.model.organizations_type import OrganizationsType

globals()["OrganizationAttributes"] = OrganizationAttributes
globals()["OrganizationsType"] = OrganizationsType
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
