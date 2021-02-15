# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.organizations_api import OrganizationsApi  # noqa: E501


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_child_org(self):
        """Test case for create_child_org

        Create a child organization  # noqa: E501
        """
        pass

    def test_get_org(self):
        """Test case for get_org

        Get organization information  # noqa: E501
        """
        pass

    def test_list_orgs(self):
        """Test case for list_orgs

        List your managed organizations  # noqa: E501
        """
        pass

    def test_update_org(self):
        """Test case for update_org

        Update your organization  # noqa: E501
        """
        pass

    def test_upload_id_p_for_org(self):
        """Test case for upload_id_p_for_org

        Upload IdP metadata  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
