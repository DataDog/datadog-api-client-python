# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.gcp_integration_api import GCPIntegrationApi  # noqa: E501


class TestGCPIntegrationApi(unittest.TestCase):
    """GCPIntegrationApi unit test stubs"""

    def setUp(self):
        self.api = GCPIntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_gcp_integration(self):
        """Test case for create_gcp_integration

        Create a GCP integration  # noqa: E501
        """
        pass

    def test_delete_gcp_integration(self):
        """Test case for delete_gcp_integration

        Delete a GCP integration  # noqa: E501
        """
        pass

    def test_list_gcp_integration(self):
        """Test case for list_gcp_integration

        List all GCP integrations  # noqa: E501
        """
        pass

    def test_update_gcp_integration(self):
        """Test case for update_gcp_integration

        Update a GCP integration  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
