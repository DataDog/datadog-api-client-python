# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import

import unittest

import datadog_api_client.v1
from datadog_api_client.v1.api.aws_logs_integration_api import AWSLogsIntegrationApi  # noqa: E501


class TestAWSLogsIntegrationApi(unittest.TestCase):
    """AWSLogsIntegrationApi unit test stubs"""

    def setUp(self):
        self.api = AWSLogsIntegrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_aws_logs_lambda_async(self):
        """Test case for check_aws_logs_lambda_async

        Check that an AWS Lambda Function exists  # noqa: E501
        """
        pass

    def test_check_aws_logs_services_async(self):
        """Test case for check_aws_logs_services_async

        Check permissions for log services  # noqa: E501
        """
        pass

    def test_create_aws_lambda_arn(self):
        """Test case for create_aws_lambda_arn

        Add AWS Log Lambda ARN  # noqa: E501
        """
        pass

    def test_delete_aws_lambda_arn(self):
        """Test case for delete_aws_lambda_arn

        Delete an AWS Logs integration  # noqa: E501
        """
        pass

    def test_enable_aws_log_services(self):
        """Test case for enable_aws_log_services

        Enable an AWS Logs integration  # noqa: E501
        """
        pass

    def test_list_aws_logs_integrations(self):
        """Test case for list_aws_logs_integrations

        List all AWS Logs integrations  # noqa: E501
        """
        pass

    def test_list_aws_logs_services(self):
        """Test case for list_aws_logs_services

        Get list of AWS log ready services  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
