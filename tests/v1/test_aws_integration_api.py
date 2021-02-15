# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi  # noqa: E501


class TestAWSIntegrationApi(unittest.TestCase):
    """AWSIntegrationApi unit test stubs"""

    def setUp(self):
        self.api = AWSIntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_aws_account(self):
        """Test case for create_aws_account

        Create an AWS integration  # noqa: E501
        """
        pass

    def test_create_aws_tag_filter(self):
        """Test case for create_aws_tag_filter

        Set an AWS tag filter  # noqa: E501
        """
        pass

    def test_create_new_aws_external_id(self):
        """Test case for create_new_aws_external_id

        Generate a new external ID  # noqa: E501
        """
        pass

    def test_delete_aws_account(self):
        """Test case for delete_aws_account

        Delete an AWS integration  # noqa: E501
        """
        pass

    def test_delete_aws_tag_filter(self):
        """Test case for delete_aws_tag_filter

        Delete a tag filtering entry  # noqa: E501
        """
        pass

    def test_list_available_aws_namespaces(self):
        """Test case for list_available_aws_namespaces

        List namespace rules  # noqa: E501
        """
        pass

    def test_list_aws_accounts(self):
        """Test case for list_aws_accounts

        List all AWS integrations  # noqa: E501
        """
        pass

    def test_list_aws_tag_filters(self):
        """Test case for list_aws_tag_filters

        Get all AWS tag filters  # noqa: E501
        """
        pass

    def test_update_aws_account(self):
        """Test case for update_aws_account

        Update an AWS integration  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
