"""
Get AWS integration IAM permissions returns "AWS IAM Permissions object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.get_aws_integration_iam_permissions()

    print(response)
