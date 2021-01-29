# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1

try:
    from datadog_api_client.v1.model import access_role
except ImportError:
    access_role = sys.modules["datadog_api_client.v1.model.access_role"]
try:
    from datadog_api_client.v1.model import organization_settings_saml
except ImportError:
    organization_settings_saml = sys.modules["datadog_api_client.v1.model.organization_settings_saml"]
try:
    from datadog_api_client.v1.model import organization_settings_saml_autocreate_users_domains
except ImportError:
    organization_settings_saml_autocreate_users_domains = sys.modules[
        "datadog_api_client.v1.model.organization_settings_saml_autocreate_users_domains"
    ]
try:
    from datadog_api_client.v1.model import organization_settings_saml_idp_initiated_login
except ImportError:
    organization_settings_saml_idp_initiated_login = sys.modules[
        "datadog_api_client.v1.model.organization_settings_saml_idp_initiated_login"
    ]
try:
    from datadog_api_client.v1.model import organization_settings_saml_strict_mode
except ImportError:
    organization_settings_saml_strict_mode = sys.modules[
        "datadog_api_client.v1.model.organization_settings_saml_strict_mode"
    ]
from datadog_api_client.v1.model.organization_settings import OrganizationSettings


class TestOrganizationSettings(unittest.TestCase):
    """OrganizationSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganizationSettings(self):
        """Test OrganizationSettings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganizationSettings()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
