# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.azure_integration_api import AzureIntegrationApi  # noqa: E501


class TestAzureIntegrationApi(unittest.TestCase):
    """AzureIntegrationApi unit test stubs"""

    def setUp(self):
        self.api = AzureIntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_azure_integration(self):
        """Test case for create_azure_integration

        Create an Azure integration  # noqa: E501
        """
        pass

    def test_delete_azure_integration(self):
        """Test case for delete_azure_integration

        Delete an Azure integration  # noqa: E501
        """
        pass

    def test_list_azure_integration(self):
        """Test case for list_azure_integration

        List all Azure integrations  # noqa: E501
        """
        pass

    def test_update_azure_host_filters(self):
        """Test case for update_azure_host_filters

        Update Azure integration host filters  # noqa: E501
        """
        pass

    def test_update_azure_integration(self):
        """Test case for update_azure_integration

        Update an Azure integration  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
